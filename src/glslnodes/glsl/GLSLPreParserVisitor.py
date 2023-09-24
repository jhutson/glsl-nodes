# Generated from GLSLPreParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GLSLPreParser import GLSLPreParser
else:
    from GLSLPreParser import GLSLPreParser

# This class defines a complete generic visitor for a parse tree produced by GLSLPreParser.

class GLSLPreParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GLSLPreParser#translation_unit.
    def visitTranslation_unit(self, ctx:GLSLPreParser.Translation_unitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#compiler_directive.
    def visitCompiler_directive(self, ctx:GLSLPreParser.Compiler_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#behavior.
    def visitBehavior(self, ctx:GLSLPreParser.BehaviorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#constant_expression.
    def visitConstant_expression(self, ctx:GLSLPreParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#define_directive.
    def visitDefine_directive(self, ctx:GLSLPreParser.Define_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#elif_directive.
    def visitElif_directive(self, ctx:GLSLPreParser.Elif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#else_directive.
    def visitElse_directive(self, ctx:GLSLPreParser.Else_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#endif_directive.
    def visitEndif_directive(self, ctx:GLSLPreParser.Endif_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#error_directive.
    def visitError_directive(self, ctx:GLSLPreParser.Error_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#error_message.
    def visitError_message(self, ctx:GLSLPreParser.Error_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#extension_directive.
    def visitExtension_directive(self, ctx:GLSLPreParser.Extension_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#extension_name.
    def visitExtension_name(self, ctx:GLSLPreParser.Extension_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#group_of_lines.
    def visitGroup_of_lines(self, ctx:GLSLPreParser.Group_of_linesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#if_directive.
    def visitIf_directive(self, ctx:GLSLPreParser.If_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#ifdef_directive.
    def visitIfdef_directive(self, ctx:GLSLPreParser.Ifdef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#ifndef_directive.
    def visitIfndef_directive(self, ctx:GLSLPreParser.Ifndef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#line_directive.
    def visitLine_directive(self, ctx:GLSLPreParser.Line_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#line_expression.
    def visitLine_expression(self, ctx:GLSLPreParser.Line_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#macro_esc_newline.
    def visitMacro_esc_newline(self, ctx:GLSLPreParser.Macro_esc_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#macro_identifier.
    def visitMacro_identifier(self, ctx:GLSLPreParser.Macro_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#macro_name.
    def visitMacro_name(self, ctx:GLSLPreParser.Macro_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#macro_text.
    def visitMacro_text(self, ctx:GLSLPreParser.Macro_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#macro_text_.
    def visitMacro_text_(self, ctx:GLSLPreParser.Macro_text_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#number.
    def visitNumber(self, ctx:GLSLPreParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#off.
    def visitOff(self, ctx:GLSLPreParser.OffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#on.
    def visitOn(self, ctx:GLSLPreParser.OnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#pragma_debug.
    def visitPragma_debug(self, ctx:GLSLPreParser.Pragma_debugContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#pragma_directive.
    def visitPragma_directive(self, ctx:GLSLPreParser.Pragma_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#pragma_optimize.
    def visitPragma_optimize(self, ctx:GLSLPreParser.Pragma_optimizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#profile.
    def visitProfile(self, ctx:GLSLPreParser.ProfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#program_text.
    def visitProgram_text(self, ctx:GLSLPreParser.Program_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#stdgl.
    def visitStdgl(self, ctx:GLSLPreParser.StdglContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#undef_directive.
    def visitUndef_directive(self, ctx:GLSLPreParser.Undef_directiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GLSLPreParser#version_directive.
    def visitVersion_directive(self, ctx:GLSLPreParser.Version_directiveContext):
        return self.visitChildren(ctx)



del GLSLPreParser