import antlr4
from . import ast
from .glsl.GLSLLexer import GLSLLexer
from .glsl.GLSLParser import GLSLParser
from .glsl.GLSLParserVisitor import GLSLParserVisitor


class UnsupportedError(Exception):

    def __init__(self, rule_type: str, text: str):
        self.rule_type = rule_type
        self.text = text


class AstBuilder(GLSLParserVisitor):

    # def visitExternal_declaration(self, ctx: GLSLParser.External_declarationContext):
    #     self.visitDeclaration(ctx.declaration())
    #
    # def visitDeclaration(self, ctx: GLSLParser.DeclarationContext):
    #     pass

    def aggregateResult(self, aggregate, next_result):
        # print(f'aggregateResult: aggregate={aggregate}, nextResult={nextResult}')
        if next_result is None:
            return aggregate
        return next_result


    def visitTranslation_unit(self, ctx: GLSLParser.Translation_unitContext):
        variables = []

        for d in ctx.external_declaration():
            node = self.visitExternal_declaration(d)
            match node:
                case ast.VariableDeclarationList():
                    variables.extend(node.variable_list)

        print(f'{variables}')
        variables_node = ast.VariableDeclarationList(variables)
        return ast.Script(variables_node)

    def visitInit_declarator_list(self, ctx: GLSLParser.Init_declarator_listContext):
        variable_list = []

        variable_node = self.visitSingle_declaration(ctx.single_declaration())
        variable_list.append(variable_node)

        for declaration in ctx.typeless_declaration():
            identifier_node = self.visitTypeless_declaration(declaration)
            variable_list.append(ast.VariableDeclaration(identifier_node, variable_node.type))

        return ast.VariableDeclarationList(variable_list)

    def visitSingle_declaration(self, ctx: GLSLParser.Single_declarationContext):
        type_node = self.visitFully_specified_type(ctx.fully_specified_type())

        typeless_declaration = ctx.typeless_declaration()
        if typeless_declaration is None:
            raise UnsupportedError("single declaration without identifier", ctx.parentCtx.getText())

        identifier_node = self.visitTypeless_declaration(typeless_declaration)
        return ast.VariableDeclaration(identifier_node, type_node)

    def visitTypeless_declaration(self, ctx: GLSLParser.Typeless_declarationContext):
        identifier_node = ast.Identifier(ctx.IDENTIFIER().symbol.text)

        # TODO: build initializer expression
        self.visitChildren(ctx)

        return identifier_node

    def visitFully_specified_type(self, ctx: GLSLParser.Fully_specified_typeContext):
        specifier_node = self.visitType_specifier(ctx.type_specifier())

        qualifier_node = None
        qualifier = ctx.type_qualifier()
        if qualifier:
            qualifier_node = self.visitType_qualifier(qualifier)

        return ast.TypeDeclaration(specifier_node, qualifier_node)

    def visitSingle_type_qualifier(self, ctx: GLSLParser.Single_type_qualifierContext):
        result = super().visitSingle_type_qualifier(ctx)
        if result is None:
            raise UnsupportedError("single type qualifier", ctx.getText())

        return result

    def visitStorage_qualifier(self, ctx: GLSLParser.Storage_qualifierContext):
        symbol = ctx.getChild(0).symbol
        match symbol.type:
            case GLSLParser.CONST | GLSLParser.IN | GLSLParser.OUT | GLSLParser.INOUT:
                return ast.TypeQualifier(symbol.text)
            case _:
                raise UnsupportedError("storage qualifier", ctx.getText())

    def visitType_specifier_nonarray(self, ctx: GLSLParser.Type_specifier_nonarrayContext):
        symbol = ctx.getChild(0).symbol
        match symbol.type:
            case GLSLParser.VOID | GLSLParser.FLOAT | GLSLParser.INT | GLSLParser.BOOL | GLSLParser.VEC3:
                return ast.TypeSpecifier(symbol.text)
            case _:
                raise UnsupportedError("type specifier", ctx.getText())

    def visitArray_specifier(self, ctx: GLSLParser.Array_specifierContext):
        raise UnsupportedError("array specifier", ctx.getText())


def load(file_path):
    input = antlr4.FileStream(file_path)
    lexer = GLSLLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = GLSLParser(stream)
    builder = AstBuilder()
    return parser.translation_unit().accept(builder)
