# Generated from GLSLPreParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GLSLPreParser import GLSLPreParser
else:
    from GLSLPreParser import GLSLPreParser

# This class defines a complete listener for a parse tree produced by GLSLPreParser.
class GLSLPreParserListener(ParseTreeListener):

    # Enter a parse tree produced by GLSLPreParser#translation_unit.
    def enterTranslation_unit(self, ctx:GLSLPreParser.Translation_unitContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#translation_unit.
    def exitTranslation_unit(self, ctx:GLSLPreParser.Translation_unitContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#compiler_directive.
    def enterCompiler_directive(self, ctx:GLSLPreParser.Compiler_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#compiler_directive.
    def exitCompiler_directive(self, ctx:GLSLPreParser.Compiler_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#behavior.
    def enterBehavior(self, ctx:GLSLPreParser.BehaviorContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#behavior.
    def exitBehavior(self, ctx:GLSLPreParser.BehaviorContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#constant_expression.
    def enterConstant_expression(self, ctx:GLSLPreParser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#constant_expression.
    def exitConstant_expression(self, ctx:GLSLPreParser.Constant_expressionContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#define_directive.
    def enterDefine_directive(self, ctx:GLSLPreParser.Define_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#define_directive.
    def exitDefine_directive(self, ctx:GLSLPreParser.Define_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#elif_directive.
    def enterElif_directive(self, ctx:GLSLPreParser.Elif_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#elif_directive.
    def exitElif_directive(self, ctx:GLSLPreParser.Elif_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#else_directive.
    def enterElse_directive(self, ctx:GLSLPreParser.Else_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#else_directive.
    def exitElse_directive(self, ctx:GLSLPreParser.Else_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#endif_directive.
    def enterEndif_directive(self, ctx:GLSLPreParser.Endif_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#endif_directive.
    def exitEndif_directive(self, ctx:GLSLPreParser.Endif_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#error_directive.
    def enterError_directive(self, ctx:GLSLPreParser.Error_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#error_directive.
    def exitError_directive(self, ctx:GLSLPreParser.Error_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#error_message.
    def enterError_message(self, ctx:GLSLPreParser.Error_messageContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#error_message.
    def exitError_message(self, ctx:GLSLPreParser.Error_messageContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#extension_directive.
    def enterExtension_directive(self, ctx:GLSLPreParser.Extension_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#extension_directive.
    def exitExtension_directive(self, ctx:GLSLPreParser.Extension_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#extension_name.
    def enterExtension_name(self, ctx:GLSLPreParser.Extension_nameContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#extension_name.
    def exitExtension_name(self, ctx:GLSLPreParser.Extension_nameContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#group_of_lines.
    def enterGroup_of_lines(self, ctx:GLSLPreParser.Group_of_linesContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#group_of_lines.
    def exitGroup_of_lines(self, ctx:GLSLPreParser.Group_of_linesContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#if_directive.
    def enterIf_directive(self, ctx:GLSLPreParser.If_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#if_directive.
    def exitIf_directive(self, ctx:GLSLPreParser.If_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#ifdef_directive.
    def enterIfdef_directive(self, ctx:GLSLPreParser.Ifdef_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#ifdef_directive.
    def exitIfdef_directive(self, ctx:GLSLPreParser.Ifdef_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#ifndef_directive.
    def enterIfndef_directive(self, ctx:GLSLPreParser.Ifndef_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#ifndef_directive.
    def exitIfndef_directive(self, ctx:GLSLPreParser.Ifndef_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#line_directive.
    def enterLine_directive(self, ctx:GLSLPreParser.Line_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#line_directive.
    def exitLine_directive(self, ctx:GLSLPreParser.Line_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#line_expression.
    def enterLine_expression(self, ctx:GLSLPreParser.Line_expressionContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#line_expression.
    def exitLine_expression(self, ctx:GLSLPreParser.Line_expressionContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#macro_esc_newline.
    def enterMacro_esc_newline(self, ctx:GLSLPreParser.Macro_esc_newlineContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#macro_esc_newline.
    def exitMacro_esc_newline(self, ctx:GLSLPreParser.Macro_esc_newlineContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#macro_identifier.
    def enterMacro_identifier(self, ctx:GLSLPreParser.Macro_identifierContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#macro_identifier.
    def exitMacro_identifier(self, ctx:GLSLPreParser.Macro_identifierContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#macro_name.
    def enterMacro_name(self, ctx:GLSLPreParser.Macro_nameContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#macro_name.
    def exitMacro_name(self, ctx:GLSLPreParser.Macro_nameContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#macro_text.
    def enterMacro_text(self, ctx:GLSLPreParser.Macro_textContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#macro_text.
    def exitMacro_text(self, ctx:GLSLPreParser.Macro_textContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#macro_text_.
    def enterMacro_text_(self, ctx:GLSLPreParser.Macro_text_Context):
        pass

    # Exit a parse tree produced by GLSLPreParser#macro_text_.
    def exitMacro_text_(self, ctx:GLSLPreParser.Macro_text_Context):
        pass


    # Enter a parse tree produced by GLSLPreParser#number.
    def enterNumber(self, ctx:GLSLPreParser.NumberContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#number.
    def exitNumber(self, ctx:GLSLPreParser.NumberContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#off.
    def enterOff(self, ctx:GLSLPreParser.OffContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#off.
    def exitOff(self, ctx:GLSLPreParser.OffContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#on.
    def enterOn(self, ctx:GLSLPreParser.OnContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#on.
    def exitOn(self, ctx:GLSLPreParser.OnContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#pragma_debug.
    def enterPragma_debug(self, ctx:GLSLPreParser.Pragma_debugContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#pragma_debug.
    def exitPragma_debug(self, ctx:GLSLPreParser.Pragma_debugContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#pragma_directive.
    def enterPragma_directive(self, ctx:GLSLPreParser.Pragma_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#pragma_directive.
    def exitPragma_directive(self, ctx:GLSLPreParser.Pragma_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#pragma_optimize.
    def enterPragma_optimize(self, ctx:GLSLPreParser.Pragma_optimizeContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#pragma_optimize.
    def exitPragma_optimize(self, ctx:GLSLPreParser.Pragma_optimizeContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#profile.
    def enterProfile(self, ctx:GLSLPreParser.ProfileContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#profile.
    def exitProfile(self, ctx:GLSLPreParser.ProfileContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#program_text.
    def enterProgram_text(self, ctx:GLSLPreParser.Program_textContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#program_text.
    def exitProgram_text(self, ctx:GLSLPreParser.Program_textContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#stdgl.
    def enterStdgl(self, ctx:GLSLPreParser.StdglContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#stdgl.
    def exitStdgl(self, ctx:GLSLPreParser.StdglContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#undef_directive.
    def enterUndef_directive(self, ctx:GLSLPreParser.Undef_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#undef_directive.
    def exitUndef_directive(self, ctx:GLSLPreParser.Undef_directiveContext):
        pass


    # Enter a parse tree produced by GLSLPreParser#version_directive.
    def enterVersion_directive(self, ctx:GLSLPreParser.Version_directiveContext):
        pass

    # Exit a parse tree produced by GLSLPreParser#version_directive.
    def exitVersion_directive(self, ctx:GLSLPreParser.Version_directiveContext):
        pass



del GLSLPreParser