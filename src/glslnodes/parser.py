import antlr4
from .glsl.GLSLLexer import GLSLLexer
from .glsl.GLSLParser import GLSLParser


def load(filePath):
    input = antlr4.FileStream(filePath)
    lexer = GLSLLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = GLSLParser(stream)
    return parser

