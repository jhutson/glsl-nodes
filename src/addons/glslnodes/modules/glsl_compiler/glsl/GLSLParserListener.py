# Generated from GLSLParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GLSLParser import GLSLParser
else:
    from GLSLParser import GLSLParser

# This class defines a complete listener for a parse tree produced by GLSLParser.
class GLSLParserListener(ParseTreeListener):

    # Enter a parse tree produced by GLSLParser#translation_unit.
    def enterTranslation_unit(self, ctx:GLSLParser.Translation_unitContext):
        pass

    # Exit a parse tree produced by GLSLParser#translation_unit.
    def exitTranslation_unit(self, ctx:GLSLParser.Translation_unitContext):
        pass


    # Enter a parse tree produced by GLSLParser#variable_identifier.
    def enterVariable_identifier(self, ctx:GLSLParser.Variable_identifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#variable_identifier.
    def exitVariable_identifier(self, ctx:GLSLParser.Variable_identifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#primary_expression.
    def enterPrimary_expression(self, ctx:GLSLParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#primary_expression.
    def exitPrimary_expression(self, ctx:GLSLParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#postfix_expression.
    def enterPostfix_expression(self, ctx:GLSLParser.Postfix_expressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#postfix_expression.
    def exitPostfix_expression(self, ctx:GLSLParser.Postfix_expressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#field_selection.
    def enterField_selection(self, ctx:GLSLParser.Field_selectionContext):
        pass

    # Exit a parse tree produced by GLSLParser#field_selection.
    def exitField_selection(self, ctx:GLSLParser.Field_selectionContext):
        pass


    # Enter a parse tree produced by GLSLParser#integer_expression.
    def enterInteger_expression(self, ctx:GLSLParser.Integer_expressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#integer_expression.
    def exitInteger_expression(self, ctx:GLSLParser.Integer_expressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#function_call.
    def enterFunction_call(self, ctx:GLSLParser.Function_callContext):
        pass

    # Exit a parse tree produced by GLSLParser#function_call.
    def exitFunction_call(self, ctx:GLSLParser.Function_callContext):
        pass


    # Enter a parse tree produced by GLSLParser#function_identifier.
    def enterFunction_identifier(self, ctx:GLSLParser.Function_identifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#function_identifier.
    def exitFunction_identifier(self, ctx:GLSLParser.Function_identifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#function_call_parameters.
    def enterFunction_call_parameters(self, ctx:GLSLParser.Function_call_parametersContext):
        pass

    # Exit a parse tree produced by GLSLParser#function_call_parameters.
    def exitFunction_call_parameters(self, ctx:GLSLParser.Function_call_parametersContext):
        pass


    # Enter a parse tree produced by GLSLParser#unary_expression.
    def enterUnary_expression(self, ctx:GLSLParser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#unary_expression.
    def exitUnary_expression(self, ctx:GLSLParser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#unary_operator.
    def enterUnary_operator(self, ctx:GLSLParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by GLSLParser#unary_operator.
    def exitUnary_operator(self, ctx:GLSLParser.Unary_operatorContext):
        pass


    # Enter a parse tree produced by GLSLParser#assignment_expression.
    def enterAssignment_expression(self, ctx:GLSLParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#assignment_expression.
    def exitAssignment_expression(self, ctx:GLSLParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#assignment_operator.
    def enterAssignment_operator(self, ctx:GLSLParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by GLSLParser#assignment_operator.
    def exitAssignment_operator(self, ctx:GLSLParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by GLSLParser#binary_expression.
    def enterBinary_expression(self, ctx:GLSLParser.Binary_expressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#binary_expression.
    def exitBinary_expression(self, ctx:GLSLParser.Binary_expressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#expression.
    def enterExpression(self, ctx:GLSLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#expression.
    def exitExpression(self, ctx:GLSLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#constant_expression.
    def enterConstant_expression(self, ctx:GLSLParser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by GLSLParser#constant_expression.
    def exitConstant_expression(self, ctx:GLSLParser.Constant_expressionContext):
        pass


    # Enter a parse tree produced by GLSLParser#declaration.
    def enterDeclaration(self, ctx:GLSLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GLSLParser#declaration.
    def exitDeclaration(self, ctx:GLSLParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GLSLParser#identifier_list.
    def enterIdentifier_list(self, ctx:GLSLParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#identifier_list.
    def exitIdentifier_list(self, ctx:GLSLParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#function_prototype.
    def enterFunction_prototype(self, ctx:GLSLParser.Function_prototypeContext):
        pass

    # Exit a parse tree produced by GLSLParser#function_prototype.
    def exitFunction_prototype(self, ctx:GLSLParser.Function_prototypeContext):
        pass


    # Enter a parse tree produced by GLSLParser#function_parameters.
    def enterFunction_parameters(self, ctx:GLSLParser.Function_parametersContext):
        pass

    # Exit a parse tree produced by GLSLParser#function_parameters.
    def exitFunction_parameters(self, ctx:GLSLParser.Function_parametersContext):
        pass


    # Enter a parse tree produced by GLSLParser#parameter_declarator.
    def enterParameter_declarator(self, ctx:GLSLParser.Parameter_declaratorContext):
        pass

    # Exit a parse tree produced by GLSLParser#parameter_declarator.
    def exitParameter_declarator(self, ctx:GLSLParser.Parameter_declaratorContext):
        pass


    # Enter a parse tree produced by GLSLParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:GLSLParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by GLSLParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:GLSLParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by GLSLParser#parameter_type_specifier.
    def enterParameter_type_specifier(self, ctx:GLSLParser.Parameter_type_specifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#parameter_type_specifier.
    def exitParameter_type_specifier(self, ctx:GLSLParser.Parameter_type_specifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#init_declarator_list.
    def enterInit_declarator_list(self, ctx:GLSLParser.Init_declarator_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#init_declarator_list.
    def exitInit_declarator_list(self, ctx:GLSLParser.Init_declarator_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#single_declaration.
    def enterSingle_declaration(self, ctx:GLSLParser.Single_declarationContext):
        pass

    # Exit a parse tree produced by GLSLParser#single_declaration.
    def exitSingle_declaration(self, ctx:GLSLParser.Single_declarationContext):
        pass


    # Enter a parse tree produced by GLSLParser#typeless_declaration.
    def enterTypeless_declaration(self, ctx:GLSLParser.Typeless_declarationContext):
        pass

    # Exit a parse tree produced by GLSLParser#typeless_declaration.
    def exitTypeless_declaration(self, ctx:GLSLParser.Typeless_declarationContext):
        pass


    # Enter a parse tree produced by GLSLParser#fully_specified_type.
    def enterFully_specified_type(self, ctx:GLSLParser.Fully_specified_typeContext):
        pass

    # Exit a parse tree produced by GLSLParser#fully_specified_type.
    def exitFully_specified_type(self, ctx:GLSLParser.Fully_specified_typeContext):
        pass


    # Enter a parse tree produced by GLSLParser#invariant_qualifier.
    def enterInvariant_qualifier(self, ctx:GLSLParser.Invariant_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#invariant_qualifier.
    def exitInvariant_qualifier(self, ctx:GLSLParser.Invariant_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#interpolation_qualifier.
    def enterInterpolation_qualifier(self, ctx:GLSLParser.Interpolation_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#interpolation_qualifier.
    def exitInterpolation_qualifier(self, ctx:GLSLParser.Interpolation_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#layout_qualifier.
    def enterLayout_qualifier(self, ctx:GLSLParser.Layout_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#layout_qualifier.
    def exitLayout_qualifier(self, ctx:GLSLParser.Layout_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#layout_qualifier_id_list.
    def enterLayout_qualifier_id_list(self, ctx:GLSLParser.Layout_qualifier_id_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#layout_qualifier_id_list.
    def exitLayout_qualifier_id_list(self, ctx:GLSLParser.Layout_qualifier_id_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#layout_qualifier_id.
    def enterLayout_qualifier_id(self, ctx:GLSLParser.Layout_qualifier_idContext):
        pass

    # Exit a parse tree produced by GLSLParser#layout_qualifier_id.
    def exitLayout_qualifier_id(self, ctx:GLSLParser.Layout_qualifier_idContext):
        pass


    # Enter a parse tree produced by GLSLParser#precise_qualifier.
    def enterPrecise_qualifier(self, ctx:GLSLParser.Precise_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#precise_qualifier.
    def exitPrecise_qualifier(self, ctx:GLSLParser.Precise_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#type_qualifier.
    def enterType_qualifier(self, ctx:GLSLParser.Type_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#type_qualifier.
    def exitType_qualifier(self, ctx:GLSLParser.Type_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#single_type_qualifier.
    def enterSingle_type_qualifier(self, ctx:GLSLParser.Single_type_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#single_type_qualifier.
    def exitSingle_type_qualifier(self, ctx:GLSLParser.Single_type_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#storage_qualifier.
    def enterStorage_qualifier(self, ctx:GLSLParser.Storage_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#storage_qualifier.
    def exitStorage_qualifier(self, ctx:GLSLParser.Storage_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#type_name_list.
    def enterType_name_list(self, ctx:GLSLParser.Type_name_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#type_name_list.
    def exitType_name_list(self, ctx:GLSLParser.Type_name_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#type_name.
    def enterType_name(self, ctx:GLSLParser.Type_nameContext):
        pass

    # Exit a parse tree produced by GLSLParser#type_name.
    def exitType_name(self, ctx:GLSLParser.Type_nameContext):
        pass


    # Enter a parse tree produced by GLSLParser#type_specifier.
    def enterType_specifier(self, ctx:GLSLParser.Type_specifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#type_specifier.
    def exitType_specifier(self, ctx:GLSLParser.Type_specifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#array_specifier.
    def enterArray_specifier(self, ctx:GLSLParser.Array_specifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#array_specifier.
    def exitArray_specifier(self, ctx:GLSLParser.Array_specifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#dimension.
    def enterDimension(self, ctx:GLSLParser.DimensionContext):
        pass

    # Exit a parse tree produced by GLSLParser#dimension.
    def exitDimension(self, ctx:GLSLParser.DimensionContext):
        pass


    # Enter a parse tree produced by GLSLParser#type_specifier_nonarray.
    def enterType_specifier_nonarray(self, ctx:GLSLParser.Type_specifier_nonarrayContext):
        pass

    # Exit a parse tree produced by GLSLParser#type_specifier_nonarray.
    def exitType_specifier_nonarray(self, ctx:GLSLParser.Type_specifier_nonarrayContext):
        pass


    # Enter a parse tree produced by GLSLParser#precision_qualifier.
    def enterPrecision_qualifier(self, ctx:GLSLParser.Precision_qualifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#precision_qualifier.
    def exitPrecision_qualifier(self, ctx:GLSLParser.Precision_qualifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#struct_specifier.
    def enterStruct_specifier(self, ctx:GLSLParser.Struct_specifierContext):
        pass

    # Exit a parse tree produced by GLSLParser#struct_specifier.
    def exitStruct_specifier(self, ctx:GLSLParser.Struct_specifierContext):
        pass


    # Enter a parse tree produced by GLSLParser#struct_declaration_list.
    def enterStruct_declaration_list(self, ctx:GLSLParser.Struct_declaration_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#struct_declaration_list.
    def exitStruct_declaration_list(self, ctx:GLSLParser.Struct_declaration_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#struct_declaration.
    def enterStruct_declaration(self, ctx:GLSLParser.Struct_declarationContext):
        pass

    # Exit a parse tree produced by GLSLParser#struct_declaration.
    def exitStruct_declaration(self, ctx:GLSLParser.Struct_declarationContext):
        pass


    # Enter a parse tree produced by GLSLParser#struct_declarator_list.
    def enterStruct_declarator_list(self, ctx:GLSLParser.Struct_declarator_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#struct_declarator_list.
    def exitStruct_declarator_list(self, ctx:GLSLParser.Struct_declarator_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#struct_declarator.
    def enterStruct_declarator(self, ctx:GLSLParser.Struct_declaratorContext):
        pass

    # Exit a parse tree produced by GLSLParser#struct_declarator.
    def exitStruct_declarator(self, ctx:GLSLParser.Struct_declaratorContext):
        pass


    # Enter a parse tree produced by GLSLParser#initializer.
    def enterInitializer(self, ctx:GLSLParser.InitializerContext):
        pass

    # Exit a parse tree produced by GLSLParser#initializer.
    def exitInitializer(self, ctx:GLSLParser.InitializerContext):
        pass


    # Enter a parse tree produced by GLSLParser#initializer_list.
    def enterInitializer_list(self, ctx:GLSLParser.Initializer_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#initializer_list.
    def exitInitializer_list(self, ctx:GLSLParser.Initializer_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#declaration_statement.
    def enterDeclaration_statement(self, ctx:GLSLParser.Declaration_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#declaration_statement.
    def exitDeclaration_statement(self, ctx:GLSLParser.Declaration_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#statement.
    def enterStatement(self, ctx:GLSLParser.StatementContext):
        pass

    # Exit a parse tree produced by GLSLParser#statement.
    def exitStatement(self, ctx:GLSLParser.StatementContext):
        pass


    # Enter a parse tree produced by GLSLParser#simple_statement.
    def enterSimple_statement(self, ctx:GLSLParser.Simple_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#simple_statement.
    def exitSimple_statement(self, ctx:GLSLParser.Simple_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#compound_statement.
    def enterCompound_statement(self, ctx:GLSLParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#compound_statement.
    def exitCompound_statement(self, ctx:GLSLParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#statement_no_new_scope.
    def enterStatement_no_new_scope(self, ctx:GLSLParser.Statement_no_new_scopeContext):
        pass

    # Exit a parse tree produced by GLSLParser#statement_no_new_scope.
    def exitStatement_no_new_scope(self, ctx:GLSLParser.Statement_no_new_scopeContext):
        pass


    # Enter a parse tree produced by GLSLParser#compound_statement_no_new_scope.
    def enterCompound_statement_no_new_scope(self, ctx:GLSLParser.Compound_statement_no_new_scopeContext):
        pass

    # Exit a parse tree produced by GLSLParser#compound_statement_no_new_scope.
    def exitCompound_statement_no_new_scope(self, ctx:GLSLParser.Compound_statement_no_new_scopeContext):
        pass


    # Enter a parse tree produced by GLSLParser#statement_list.
    def enterStatement_list(self, ctx:GLSLParser.Statement_listContext):
        pass

    # Exit a parse tree produced by GLSLParser#statement_list.
    def exitStatement_list(self, ctx:GLSLParser.Statement_listContext):
        pass


    # Enter a parse tree produced by GLSLParser#expression_statement.
    def enterExpression_statement(self, ctx:GLSLParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#expression_statement.
    def exitExpression_statement(self, ctx:GLSLParser.Expression_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#selection_statement.
    def enterSelection_statement(self, ctx:GLSLParser.Selection_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#selection_statement.
    def exitSelection_statement(self, ctx:GLSLParser.Selection_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#selection_rest_statement.
    def enterSelection_rest_statement(self, ctx:GLSLParser.Selection_rest_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#selection_rest_statement.
    def exitSelection_rest_statement(self, ctx:GLSLParser.Selection_rest_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#condition.
    def enterCondition(self, ctx:GLSLParser.ConditionContext):
        pass

    # Exit a parse tree produced by GLSLParser#condition.
    def exitCondition(self, ctx:GLSLParser.ConditionContext):
        pass


    # Enter a parse tree produced by GLSLParser#switch_statement.
    def enterSwitch_statement(self, ctx:GLSLParser.Switch_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#switch_statement.
    def exitSwitch_statement(self, ctx:GLSLParser.Switch_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#case_label.
    def enterCase_label(self, ctx:GLSLParser.Case_labelContext):
        pass

    # Exit a parse tree produced by GLSLParser#case_label.
    def exitCase_label(self, ctx:GLSLParser.Case_labelContext):
        pass


    # Enter a parse tree produced by GLSLParser#iteration_statement.
    def enterIteration_statement(self, ctx:GLSLParser.Iteration_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#iteration_statement.
    def exitIteration_statement(self, ctx:GLSLParser.Iteration_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#for_init_statement.
    def enterFor_init_statement(self, ctx:GLSLParser.For_init_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#for_init_statement.
    def exitFor_init_statement(self, ctx:GLSLParser.For_init_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#for_rest_statement.
    def enterFor_rest_statement(self, ctx:GLSLParser.For_rest_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#for_rest_statement.
    def exitFor_rest_statement(self, ctx:GLSLParser.For_rest_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#jump_statement.
    def enterJump_statement(self, ctx:GLSLParser.Jump_statementContext):
        pass

    # Exit a parse tree produced by GLSLParser#jump_statement.
    def exitJump_statement(self, ctx:GLSLParser.Jump_statementContext):
        pass


    # Enter a parse tree produced by GLSLParser#external_declaration.
    def enterExternal_declaration(self, ctx:GLSLParser.External_declarationContext):
        pass

    # Exit a parse tree produced by GLSLParser#external_declaration.
    def exitExternal_declaration(self, ctx:GLSLParser.External_declarationContext):
        pass


    # Enter a parse tree produced by GLSLParser#function_definition.
    def enterFunction_definition(self, ctx:GLSLParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by GLSLParser#function_definition.
    def exitFunction_definition(self, ctx:GLSLParser.Function_definitionContext):
        pass



del GLSLParser