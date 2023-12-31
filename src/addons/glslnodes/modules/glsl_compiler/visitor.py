from typing import Dict, Optional, Tuple

from . import graph
from .glsl_ast import *

_math_operation_from_symbol = {
    '+': 'ADD',
    '-': 'SUBTRACT',
    '*': 'MULTIPLY',
    '/': 'DIVIDE'
}

_builtin_functions = {
    'sin': 'SINE',
    'cos': 'COSINE',
    'tan': 'TANGENT',
    'radians': 'RADIANS',
    'degrees': 'DEGREES',
    'asin': 'ARCSINE',
    'acos': 'ARCCOSINE',
    'atan': ['ARCTANGENT', 'ARCTAN2'],  # For one and two parameters, respectively.
    'sinh': 'SINH',
    'cosh': 'COSH',
    'tanh': 'TANH'
}


class SymbolTable:
    declarations: Dict[str, VariableDeclaration]
    bindings: Dict[str, Tuple[graph.SocketRef, bool]]
    parent: Optional['SymbolTable']

    def __init__(self, parent: Optional['SymbolTable'] = None):
        self.declarations = dict()
        self.bindings = dict()
        self.parent = parent

    def add_declaration(self, declaration: VariableDeclaration,
                        value: Optional[graph.SocketRef] = None, immutable: bool = False):
        name = declaration.identifier.name
        if name not in self.declarations:
            self.declarations[name] = declaration

            if value:
                self.bindings[name] = (value, immutable)
        else:
            raise ValueError(f"Variable declaration for '{name}' already exists in symbol table")

    def _find_table_for_declaration(self, name: str):
        table = self
        while table is not None:
            if name in table.declarations:
                return table
            table = table.parent
        raise ValueError(f"Variable declaration not found for '{name}'")

    def set_binding(self, identifier: Identifier, value: graph.SocketRef):
        name = identifier.name
        table = self._find_table_for_declaration(name)
        if table.bindings[name][1]:
            raise ValueError(f"Cannot change value of immutable variable '{name}'")
        table.bindings[name] = (value, False)

    def get_binding(self, identifier: Identifier):
        name = identifier.name
        table = self._find_table_for_declaration(name)
        return table.bindings.get(name)[0]


def _get_socket_type(node: VariableDeclaration | ConstantExpression):
    type_name = ""
    variable_name = ""

    match node:
        case VariableDeclaration(type=TypeDeclaration(specifier=TypeSpecifier(name))):
            type_name = name
            variable_name = node.identifier.name
        case ConstantExpression(type=TypeSpecifier(name)):
            type_name = name
        case _:
            raise ValueError(f"Unexpected node type {type(node)}")

    match type_name:
        case 'float':
            return "NodeSocketFloat"
        case 'int':
            return "NodeSocketInt"
        case _:
            message = f"Unsupported mapping from '{type_name}' to node socket type"
            if variable_name:
                message += f" for variable '{variable_name}'"
            raise ValueError(message)


class GraphBuilder(GlslVisitor):
    node_graph: graph.NodeGraph
    _environment: List[SymbolTable]

    def _current_scope(self):
        return self._environment[-1]

    def visit_script(self, node: Script):
        self._environment = [SymbolTable()]
        self.node_graph = graph.NodeGraph()

        super().visit_script(node)

        # Link group outputs based on bindings.
        top = self._current_scope()
        group_output = self.node_graph.get_group_output()
        outputs_by_name = {s.name: i for i, s in enumerate(group_output.inputs)}
        for name in top.bindings:
            socket_ref, immutable = top.bindings[name]
            if not immutable and socket_ref.node != group_output:
                to_socket = graph.SocketRef(outputs_by_name[name], group_output)
                self.node_graph.links[to_socket].append(socket_ref)

    def visit_identifier(self, node: Identifier):
        super().visit_identifier(node)

    def visit_type_specifier(self, node: TypeSpecifier):
        super().visit_type_specifier(node)

    def visit_type_qualifier(self, node: TypeQualifier):
        super().visit_type_qualifier(node)

    def visit_type_declaration(self, node: TypeDeclaration):
        super().visit_type_declaration(node)

    def visit_variable_declaration(self, node: VariableDeclaration):
        qualifier = node.type.qualifier
        if len(self._environment) == 1:  # global variables
            if qualifier:
                match qualifier.name:
                    case 'in':
                        socket = graph.Socket(node.identifier.name, _get_socket_type(node))
                        group_input = self.node_graph.get_group_input()
                        index = len(group_input.outputs)
                        group_input.outputs.append(socket)
                        self._current_scope().add_declaration(node, graph.SocketRef(index, group_input), True)
                        return
                    case 'out':
                        socket = graph.Socket(node.identifier.name, _get_socket_type(node))
                        group_output = self.node_graph.get_group_output()
                        index = len(group_output.inputs)
                        group_output.inputs.append(socket)
                        self._current_scope().add_declaration(node, graph.SocketRef(index, group_output))
                        return

        if node.initializer:
            socket_ref = node.initializer.accept(self)
            immutable = qualifier is not None and qualifier.name == 'const'
            self._current_scope().add_declaration(node, socket_ref, immutable)
        else:
            self._current_scope().add_declaration(node)

    def visit_variable_declaration_list(self, node: VariableDeclarationList):
        super().visit_variable_declaration_list(node)

    def visit_function_declaration(self, node: FunctionDeclaration):
        function_scope = SymbolTable(self._current_scope())
        self._environment.append(function_scope)
        super().visit_function_declaration(node)
        self._environment.pop()

    def visit_identifier_expression(self, node: IdentifierExpression):
        return self._current_scope().get_binding(node.identifier)

    def visit_integer_expression(self, node: IntegerExpression):
        value_node = graph.ValueNode(node.value)
        self.node_graph.nodes.append(value_node)
        return graph.SocketRef(0, value_node)

    def visit_float_expression(self, node: FloatExpression):
        value_node = graph.ValueNode(node.value)
        self.node_graph.nodes.append(value_node)
        return graph.SocketRef(0, value_node)

    def visit_boolean_expression(self, node: BooleanExpression):
        super().visit_boolean_expression(node)

    def visit_expression_list(self, node: ExpressionList):
        super().visit_expression_list(node)

    def visit_unary_op_expression(self, node: UnaryOpExpression):
        super().visit_unary_op_expression(node)

    def visit_binary_op_expression(self, node: BinaryOpExpression):
        operation = _math_operation_from_symbol.get(node.operator)
        if operation is None:
            raise ValueError(f"Operator not supported: '{node.operator}'")

        left_socket = node.left.accept(self)
        right_socket = node.right.accept(self)

        math_node = graph.MathNode(operation, 2)
        self.node_graph.nodes.append(math_node)
        self.node_graph.links[graph.SocketRef(0, math_node)].append(left_socket)
        self.node_graph.links[graph.SocketRef(1, math_node)].append(right_socket)

        return graph.SocketRef(0, math_node)

    def visit_assignment_expression(self, node: AssignmentExpression):
        if not node.operator == "=":
            raise ValueError(f"not implemented: assignment operator '{node.operator}'")

        right_socket = node.right.accept(self)
        self._current_scope().set_binding(node.left.identifier, right_socket)

        return right_socket

    def visit_call_expression(self, node: CallExpression):
        function_name = node.name.identifier.name
        builtin = _builtin_functions.get(function_name)
        if builtin is None:
            raise ValueError(f"Function not defined: '{function_name}'")

        if not node.parameters or len(node.parameters.expressions) == 0:
            raise ValueError(
                f"Function '{function_name}' expects one or more parameters, but none were supplied.")

        supplied_parameter_count = len(node.parameters.expressions)

        operation: str
        match builtin:
            case list():
                if supplied_parameter_count > len(builtin):
                    raise ValueError(
                        f"Function '{function_name}' expects 1 to {len(builtin)} parameters, but {supplied_parameter_count} were supplied.")

                operation = builtin[supplied_parameter_count - 1]
            case _:
                if supplied_parameter_count > 1:
                    raise ValueError(
                        f"Function '{function_name}' expects one parameter, but {supplied_parameter_count} were supplied.")

                operation = builtin

        math_node = graph.MathNode(operation, supplied_parameter_count)
        self.node_graph.nodes.append(math_node)

        for index, expression in enumerate(node.parameters.expressions):
            socket_ref = expression.accept(self)
            self.node_graph.links[graph.SocketRef(index, math_node)].append(socket_ref)

        return graph.SocketRef(0, math_node)

    def visit_statement_list(self, node: StatementList):
        super().visit_statement_list(node)

    def visit_expression_statement(self, node: ExpressionStatement):
        super().visit_expression_statement(node)
