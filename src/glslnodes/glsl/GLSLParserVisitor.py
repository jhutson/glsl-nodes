# Generated from GLSLParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GLSLParser import GLSLParser
else:
    from GLSLParser import GLSLParser

# This class defines a complete generic visitor for a parse tree produced by GLSLParser.

class GLSLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GLSLParser#translation_unit.
    def visitTranslation_unit(self, ctx:GLSLParser.Translation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#variable_identifier.
    def visitVariable_identifier(self, ctx:GLSLParser.Variable_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#primary_expression.
    def visitPrimary_expression(self, ctx:GLSLParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#postfix_expression.
    def visitPostfix_expression(self, ctx:GLSLParser.Postfix_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#field_selection.
    def visitField_selection(self, ctx:GLSLParser.Field_selectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#integer_expression.
    def visitInteger_expression(self, ctx:GLSLParser.Integer_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#function_call.
    def visitFunction_call(self, ctx:GLSLParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#function_identifier.
    def visitFunction_identifier(self, ctx:GLSLParser.Function_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#function_call_parameters.
    def visitFunction_call_parameters(self, ctx:GLSLParser.Function_call_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#unary_expression.
    def visitUnary_expression(self, ctx:GLSLParser.Unary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#unary_operator.
    def visitUnary_operator(self, ctx:GLSLParser.Unary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#assignment_expression.
    def visitAssignment_expression(self, ctx:GLSLParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#assignment_operator.
    def visitAssignment_operator(self, ctx:GLSLParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#binary_expression.
    def visitBinary_expression(self, ctx:GLSLParser.Binary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#expression.
    def visitExpression(self, ctx:GLSLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#constant_expression.
    def visitConstant_expression(self, ctx:GLSLParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#declaration.
    def visitDeclaration(self, ctx:GLSLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#identifier_list.
    def visitIdentifier_list(self, ctx:GLSLParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#function_prototype.
    def visitFunction_prototype(self, ctx:GLSLParser.Function_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#function_parameters.
    def visitFunction_parameters(self, ctx:GLSLParser.Function_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#parameter_declarator.
    def visitParameter_declarator(self, ctx:GLSLParser.Parameter_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:GLSLParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#parameter_type_specifier.
    def visitParameter_type_specifier(self, ctx:GLSLParser.Parameter_type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#init_declarator_list.
    def visitInit_declarator_list(self, ctx:GLSLParser.Init_declarator_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#single_declaration.
    def visitSingle_declaration(self, ctx:GLSLParser.Single_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#typeless_declaration.
    def visitTypeless_declaration(self, ctx:GLSLParser.Typeless_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#fully_specified_type.
    def visitFully_specified_type(self, ctx:GLSLParser.Fully_specified_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#invariant_qualifier.
    def visitInvariant_qualifier(self, ctx:GLSLParser.Invariant_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#interpolation_qualifier.
    def visitInterpolation_qualifier(self, ctx:GLSLParser.Interpolation_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#layout_qualifier.
    def visitLayout_qualifier(self, ctx:GLSLParser.Layout_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#layout_qualifier_id_list.
    def visitLayout_qualifier_id_list(self, ctx:GLSLParser.Layout_qualifier_id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#layout_qualifier_id.
    def visitLayout_qualifier_id(self, ctx:GLSLParser.Layout_qualifier_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#precise_qualifier.
    def visitPrecise_qualifier(self, ctx:GLSLParser.Precise_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#type_qualifier.
    def visitType_qualifier(self, ctx:GLSLParser.Type_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#single_type_qualifier.
    def visitSingle_type_qualifier(self, ctx:GLSLParser.Single_type_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#storage_qualifier.
    def visitStorage_qualifier(self, ctx:GLSLParser.Storage_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#type_name_list.
    def visitType_name_list(self, ctx:GLSLParser.Type_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#type_name.
    def visitType_name(self, ctx:GLSLParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#type_specifier.
    def visitType_specifier(self, ctx:GLSLParser.Type_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#array_specifier.
    def visitArray_specifier(self, ctx:GLSLParser.Array_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#dimension.
    def visitDimension(self, ctx:GLSLParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#type_specifier_nonarray.
    def visitType_specifier_nonarray(self, ctx:GLSLParser.Type_specifier_nonarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#precision_qualifier.
    def visitPrecision_qualifier(self, ctx:GLSLParser.Precision_qualifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#struct_specifier.
    def visitStruct_specifier(self, ctx:GLSLParser.Struct_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#struct_declaration_list.
    def visitStruct_declaration_list(self, ctx:GLSLParser.Struct_declaration_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#struct_declaration.
    def visitStruct_declaration(self, ctx:GLSLParser.Struct_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#struct_declarator_list.
    def visitStruct_declarator_list(self, ctx:GLSLParser.Struct_declarator_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#struct_declarator.
    def visitStruct_declarator(self, ctx:GLSLParser.Struct_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#initializer.
    def visitInitializer(self, ctx:GLSLParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#initializer_list.
    def visitInitializer_list(self, ctx:GLSLParser.Initializer_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#declaration_statement.
    def visitDeclaration_statement(self, ctx:GLSLParser.Declaration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#statement.
    def visitStatement(self, ctx:GLSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#simple_statement.
    def visitSimple_statement(self, ctx:GLSLParser.Simple_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#compound_statement.
    def visitCompound_statement(self, ctx:GLSLParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#statement_no_new_scope.
    def visitStatement_no_new_scope(self, ctx:GLSLParser.Statement_no_new_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#compound_statement_no_new_scope.
    def visitCompound_statement_no_new_scope(self, ctx:GLSLParser.Compound_statement_no_new_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#statement_list.
    def visitStatement_list(self, ctx:GLSLParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#expression_statement.
    def visitExpression_statement(self, ctx:GLSLParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#selection_statement.
    def visitSelection_statement(self, ctx:GLSLParser.Selection_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#selection_rest_statement.
    def visitSelection_rest_statement(self, ctx:GLSLParser.Selection_rest_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#condition.
    def visitCondition(self, ctx:GLSLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#switch_statement.
    def visitSwitch_statement(self, ctx:GLSLParser.Switch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#case_label.
    def visitCase_label(self, ctx:GLSLParser.Case_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#iteration_statement.
    def visitIteration_statement(self, ctx:GLSLParser.Iteration_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#for_init_statement.
    def visitFor_init_statement(self, ctx:GLSLParser.For_init_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#for_rest_statement.
    def visitFor_rest_statement(self, ctx:GLSLParser.For_rest_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#jump_statement.
    def visitJump_statement(self, ctx:GLSLParser.Jump_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#external_declaration.
    def visitExternal_declaration(self, ctx:GLSLParser.External_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLParser#function_definition.
    def visitFunction_definition(self, ctx:GLSLParser.Function_definitionContext):
        return self.visitChildren(ctx)



del GLSLParser