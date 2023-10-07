from dataclasses import dataclass
from typing import List, Optional


class Node:

    def accept(self, visitor: 'GlslVisitor'):
        pass


class Expression(Node):
    pass


@dataclass
class ExpressionList(Node):
    expressions: List[Expression]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_expression_list(self)


@dataclass
class UnaryOpExpression(Expression):
    expression: Expression
    operator: str

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_unary_op_expression(self)


@dataclass
class BinaryOpExpression(Expression):
    left: Expression
    right: Expression
    operator: str

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_binary_op_expression(self)


@dataclass()
class Identifier(Node):
    name: str

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_identifier(self)


@dataclass()
class IdentifierExpression(Expression):
    identifier: Identifier

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_identifier_expression(self)


@dataclass
class AssignmentExpression(Expression):
    left: IdentifierExpression
    right: Expression
    operator: str

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_assignment_expression(self)


@dataclass
class CallExpression(Expression):
    name: IdentifierExpression
    parameters: Optional[ExpressionList]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_call_expression(self)


@dataclass()
class TypeSpecifier(Node):
    name: str

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_type_specifier(self)


@dataclass()
class TypeQualifier(Node):
    name: str

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_type_qualifier(self)


@dataclass
class TypeDeclaration(Node):
    specifier: TypeSpecifier
    qualifier: Optional[TypeQualifier]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_type_declaration(self)


@dataclass
class VariableDeclaration(Node):
    identifier: Identifier
    type: TypeDeclaration
    initializer: Optional[Expression]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_variable_declaration(self)


@dataclass
class VariableDeclarationList(Node):
    variables: List[VariableDeclaration]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_variable_declaration_list(self)


@dataclass
class ConstantExpression(Expression):
    type: TypeSpecifier


@dataclass
class IntegerExpression(ConstantExpression):
    value: int

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_integer_expression(self)


@dataclass
class FloatExpression(ConstantExpression):
    value: float

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_float_expression(self)


@dataclass
class BooleanExpression(ConstantExpression):
    value: bool

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_boolean_expression(self)


class Statement(Node):
    pass


@dataclass
class StatementList(Statement):
    statements: List[Statement]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_statement_list(self)


@dataclass
class ExpressionStatement(Statement):
    expression: Expression

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_expression_statement(self)


@dataclass
class FunctionDeclaration(Node):
    name: Identifier
    return_type: TypeDeclaration
    parameters: Optional[List[VariableDeclaration]]
    body: Statement

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_function_declaration(self)


@dataclass
class Script(Node):
    variable_list: VariableDeclarationList
    functions: List[FunctionDeclaration]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_script(self)


class GlslVisitor(Node):

    def visit_identifier(self, node: Identifier):
        pass

    def visit_type_specifier(self, node: TypeSpecifier):
        pass

    def visit_type_qualifier(self, node: TypeQualifier):
        pass

    def visit_type_declaration(self, node: TypeDeclaration):
        self.visit_type_specifier(node.specifier)
        if node.qualifier:
            self.visit_type_qualifier(node.qualifier)

    def visit_variable_declaration(self, node: VariableDeclaration):
        self.visit_identifier(node.identifier)
        self.visit_type_declaration(node.type)
        if node.initializer:
            node.initializer.accept(self)

    def visit_variable_declaration_list(self, node: VariableDeclarationList):
        for v in node.variables:
            self.visit_variable_declaration(v)

    def visit_function_declaration(self, node: FunctionDeclaration):
        self.visit_identifier(node.name)
        self.visit_type_declaration(node.return_type)
        if node.parameters:
            for parameter in node.parameters:
                parameter.accept(self)
        node.body.accept(self)

    def visit_identifier_expression(self, node: IdentifierExpression):
        self.visit_identifier(node.identifier)

    def visit_integer_expression(self, node: IntegerExpression):
        self.visit_type_specifier(node.type)

    def visit_float_expression(self, node: FloatExpression):
        self.visit_type_specifier(node.type)

    def visit_boolean_expression(self, node: BooleanExpression):
        self.visit_type_specifier(node.type)

    def visit_expression_list(self, node: ExpressionList):
        for e in node.expressions:
            e.accept(self)

    def visit_unary_op_expression(self, node: UnaryOpExpression):
        node.expression.accept(self)

    def visit_binary_op_expression(self, node: BinaryOpExpression):
        node.left.accept(self)
        node.right.accept(self)

    def visit_assignment_expression(self, node: AssignmentExpression):
        node.left.accept(self)
        node.right.accept(self)

    def visit_call_expression(self, node: CallExpression):
        self.visit_identifier_expression(node.name)
        if node.parameters:
            self.visit_expression_list(node.parameters)

    def visit_statement_list(self, node: StatementList):
        for s in node.statements:
            s.accept(self)

    def visit_expression_statement(self, node: ExpressionStatement):
        node.expression.accept(self)

    def visit_script(self, node: Script):
        self.visit_variable_declaration_list(node.variable_list)
        for f in node.functions:
            f.accept(self)

