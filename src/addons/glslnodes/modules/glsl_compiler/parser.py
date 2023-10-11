import antlr4
from . import glsl_ast as ast
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
        function_declarations = []

        for d in ctx.external_declaration():
            node = self.visitExternal_declaration(d)
            match node:
                case ast.VariableDeclarationList():
                    variables.extend(node.variables)
                case ast.FunctionDeclaration():
                    function_declarations.append(node)

        # print(f'{variables}')
        variables_node = ast.VariableDeclarationList(variables)
        return ast.Script(variables_node, function_declarations)

    def visitFunction_definition(self, ctx:GLSLParser.Function_definitionContext):
        prototype: ast.FunctionDeclaration = ctx.function_prototype().accept(self)
        body = ctx.compound_statement_no_new_scope().accept(self)

        return ast.FunctionDeclaration(
            prototype.name,
            prototype.return_type,
            prototype.parameters,
            body
        )

    def visitFunction_prototype(self, ctx:GLSLParser.Function_prototypeContext):
        return_type = self.visitFully_specified_type(ctx.fully_specified_type())
        identifier_node = ast.Identifier(ctx.IDENTIFIER().symbol.text)

        parameters_node = None
        parameters = ctx.function_parameters()
        if parameters:
            parameters_node = parameters.accept(self)

        return ast.FunctionDeclaration(identifier_node, return_type, parameters_node, ast.Statement())

    def visitFunction_parameters(self, ctx:GLSLParser.Function_parametersContext):
        parameters = [d.accept(self) for d in ctx.parameter_declaration()]
        return ast.VariableDeclarationList(parameters)

    def visitParameter_declarator(self, ctx:GLSLParser.Parameter_declaratorContext):
        if ctx.array_specifier():
            raise UnsupportedError("array specifier", ctx.getText())

        specifier_node = self.visitType_specifier(ctx.type_specifier())
        identifier_node = ast.Identifier(ctx.IDENTIFIER().symbol.text)

        type_node = ast.TypeDeclaration(specifier_node, None)
        return ast.VariableDeclaration(identifier_node, type_node, None)

    def visitParameter_declaration(self, ctx:GLSLParser.Parameter_declarationContext):
        first = ctx.getChild(0)
        if isinstance(first, GLSLParser.Parameter_declaratorContext):
            return self.visitParameter_declarator(first)

        raise UnsupportedError("parameter declaration", ctx.getText())

    def visitInit_declarator_list(self, ctx: GLSLParser.Init_declarator_listContext):
        variable_list = []

        variable_node = self.visitSingle_declaration(ctx.single_declaration())
        variable_list.append(variable_node)

        for declaration in ctx.typeless_declaration():
            identifier_node = ast.Identifier(declaration.IDENTIFIER().symbol.text)
            initializer_node = self.visitTypeless_declaration(declaration)
            variable_list.append(ast.VariableDeclaration(identifier_node, variable_node.type, initializer_node))

        return ast.VariableDeclarationList(variable_list)

    def visitSingle_declaration(self, ctx: GLSLParser.Single_declarationContext):
        type_node = self.visitFully_specified_type(ctx.fully_specified_type())

        typeless_declaration = ctx.typeless_declaration()
        if typeless_declaration is None:
            raise UnsupportedError("single declaration without identifier", ctx.parentCtx.getText())

        identifier_node = ast.Identifier(typeless_declaration.IDENTIFIER().symbol.text)
        initializer_node = self.visitTypeless_declaration(typeless_declaration)
        return ast.VariableDeclaration(identifier_node, type_node, initializer_node)

    def visitTypeless_declaration(self, ctx: GLSLParser.Typeless_declarationContext):
        if ctx.array_specifier() is not None:
            raise UnsupportedError("array specifier", ctx.getText())

        initializer = ctx.initializer()
        if initializer is not None:
            initializer_node = initializer.accept(self)

            # TODO: Support expressions of the form "int x = y = 3"?
            if isinstance(initializer_node, ast.AssignmentExpression):
                raise UnsupportedError("chained assignment in declarations", ctx.getText())

            return initializer_node

        return None

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

    def visitVariable_identifier(self, ctx: GLSLParser.Variable_identifierContext):
        identifier_node = ast.Identifier(ctx.IDENTIFIER().symbol.text)
        return ast.IdentifierExpression(identifier_node)

    def visitBinary_expression(self, ctx: GLSLParser.Binary_expressionContext):
        op_terminal = ctx.getChild(1)
        if op_terminal:
            subexpressions = ctx.binary_expression()
            left = self.visitBinary_expression(subexpressions[0])
            right = self.visitBinary_expression(subexpressions[1])

            return ast.BinaryOpExpression(left, right, op_terminal.symbol.text)
        else:
            result = self.visitUnary_expression(ctx.unary_expression())
            if result is None:
                raise UnsupportedError("unary expression", ctx.getText())
            return result

    def visitPrimary_expression(self, ctx: GLSLParser.Primary_expressionContext):
        child = ctx.getChild(0)
        if isinstance(child, GLSLParser.Variable_identifierContext):
            return self.visitVariable_identifier(child)

        match child.symbol.type:
            case GLSLParser.TRUE:
                return ast.BooleanExpression(ast.TypeSpecifier("bool"), True)
            case GLSLParser.FALSE:
                return ast.BooleanExpression(ast.TypeSpecifier("bool"), False)
            case GLSLParser.INTCONSTANT:
                # TODO: Test converting from hex or octal constant in addition to decimal
                return ast.IntegerExpression(ast.TypeSpecifier("int"), int(child.symbol.text))
            case GLSLParser.FLOATCONSTANT | GLSLParser.DOUBLECONSTANT:
                # TODO: Test converting from values with exponent
                return ast.FloatExpression(ast.TypeSpecifier("float"), float(child.symbol.text))
            case GLSLParser.UINTCONSTANT:
                raise UnsupportedError("uint constant", ctx.getText())
            case GLSLParser.LEFT_PAREN:
                return ctx.expression().accept(self)

        return None

    def visitAssignment_expression(self, ctx: GLSLParser.Assignment_expressionContext):
        operator = ctx.assignment_operator()
        if operator is None:
            return self.visitChildren(ctx)

        left = ctx.unary_expression().accept(self)
        if left is None or not isinstance(left, ast.IdentifierExpression):
            raise UnsupportedError("left hand side of assignment expression", ctx.unary_expression().getText())

        right = ctx.assignment_expression().accept(self)
        if right is None:
            raise UnsupportedError("right hand side of assignment expression", ctx.assignment_expression().getText())

        return ast.AssignmentExpression(left, right, operator.getChild(0).symbol.text)

    def visitPostfix_expression(self, ctx: GLSLParser.Postfix_expressionContext):
        primary = ctx.primary_expression()
        if primary:
            return primary.accept(self)

        if ctx.LEFT_PAREN() and ctx.type_specifier() is None:
            first = ctx.postfix_expression().accept(self)
            if not isinstance(first, ast.IdentifierExpression):
                raise UnsupportedError("call to non-identifier", ctx.getText())

            parameters = None
            call_parameters = ctx.function_call_parameters()
            if call_parameters:
                parameters = self.visitFunction_call_parameters(call_parameters)

            return ast.CallExpression(first, parameters)

        # TODO: support other productions for this rule.
        raise UnsupportedError("postfix expression", ctx.getText())

    def visitFunction_call_parameters(self, ctx: GLSLParser.Function_call_parametersContext):
        if ctx.VOID():
            raise UnsupportedError("void as parameter", ctx.getText())

        parameters = [e.accept(self) for e in ctx.assignment_expression()]
        return ast.ExpressionList(parameters)

    def visitStatement_list(self, ctx:GLSLParser.Statement_listContext):
        statement_nodes = [s.accept(self) for s in ctx.statement()]
        return ast.StatementList(statement_nodes)

    def visitExpression_statement(self, ctx:GLSLParser.Expression_statementContext):
        expression_node = self.visitChildren(ctx)
        if expression_node:
            return ast.ExpressionStatement(expression_node)

    def visitDeclaration_statement(self, ctx:GLSLParser.Declaration_statementContext):
        declaration = self.visitChildren(ctx)
        if declaration is None:
            raise UnsupportedError("declaration statement", ctx.getText())

        return ast.DeclarationStatement(declaration)


def load(file_path) -> ast.Script:
    input = antlr4.FileStream(file_path)
    lexer = GLSLLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = GLSLParser(stream)
    builder = AstBuilder()
    return parser.translation_unit().accept(builder)
