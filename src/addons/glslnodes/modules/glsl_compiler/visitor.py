from .glsl_ast import *
from contextlib import contextmanager

def _name(item):
    return type(item).__name__

class Printer(GlslVisitor):
    _indent: int

    def __init__(self):
        self._indent = 0

    @contextmanager
    def do_indent(self):
        self._indent += 1
        try:
            yield self._indent
        finally:
            self._indent -= 1

    def print(self, message: str):
        print(f"{' '*(2*self._indent)}{message}")

    def visit_identifier(self, node: Identifier):
        self.print(f"{_name(node)}: {node.name}")

    def visit_type_specifier(self, node: TypeSpecifier):
        self.print(f"{_name(node)}: {node.name}")

    def visit_type_qualifier(self, node: TypeQualifier):
        self.print(f"{_name(node)}: {node.name}")

    def visit_type_declaration(self, node: TypeDeclaration):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_type_declaration(node)

    def visit_variable_declaration(self, node: VariableDeclaration):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_variable_declaration(node)

    def visit_variable_declaration_list(self, node: VariableDeclarationList):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_variable_declaration_list(node)

    def visit_function_declaration(self, node: FunctionDeclaration):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_function_declaration(node)

    def visit_identifier_expression(self, node: IdentifierExpression):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_identifier_expression(node)

    def visit_integer_expression(self, node: IntegerExpression):
        self.print(f"{_name(node)}: {node.value}")
        with self.do_indent():
            super().visit_integer_expression(node)

    def visit_float_expression(self, node: FloatExpression):
        self.print(f"{_name(node)}: {node.value}")
        with self.do_indent():
            super().visit_float_expression(node)

    def visit_boolean_expression(self, node: BooleanExpression):
        self.print(f"{_name(node)}: {node.value}")
        with self.do_indent():
            super().visit_boolean_expression(node)

    def visit_expression_list(self, node: ExpressionList):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_expression_list(node)

    def visit_unary_op_expression(self, node: UnaryOpExpression):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_unary_op_expression(node)

    def visit_binary_op_expression(self, node: BinaryOpExpression):
        self.print(f"{_name(node)}: {node.operator}")
        with self.do_indent():
            super().visit_binary_op_expression(node)

    def visit_assignment_expression(self, node: AssignmentExpression):
        self.print(f"{_name(node)}: {node.operator}")
        with self.do_indent():
            super().visit_assignment_expression(node)

    def visit_call_expression(self, node: CallExpression):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_call_expression(node)

    def visit_statement_list(self, node: StatementList):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_statement_list(node)

    def visit_expression_statement(self, node: ExpressionStatement):
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_expression_statement(node)

    def visit_script(self, node: Script):
        self.print("")
        self.print(f"{_name(node)}:")
        with self.do_indent():
            super().visit_script(node)