from dataclasses import dataclass
from typing import List


class Node:

    def accept(self, visitor: 'GlslVisitor'):
        pass


@dataclass()
class Identifier(Node):
    name: str

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_identifier(self)


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
    qualifier: TypeQualifier | None

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_type_declaration(self)



@dataclass
class VariableDeclaration(Node):
    identifier: Identifier
    type: TypeDeclaration

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_variable_declaration(self)

@dataclass
class VariableDeclarationList(Node):
    variables: List[VariableDeclaration]

    def accept(self, visitor: 'GlslVisitor'):
        return visitor.visit_variable_declaration_list(self)

@dataclass
class Script(Node):
    variable_list: VariableDeclarationList

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
        self.visit_type_qualifier(node.qualifier)

    def visit_variable_declaration(self, node: VariableDeclaration):
        self.visit_identifier(node.identifier)
        self.visit_type_declaration(node.type)

    def visit_variable_declaration_list(self, node: VariableDeclarationList):
        for v in node.variables:
            self.visit_variable_declaration(v)

    def visit_script(self, node: Script):
        self.visit_variable_declaration_list(node.variable_list)
