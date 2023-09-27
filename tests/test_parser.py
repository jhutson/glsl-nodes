import antlr4
from antlr4 import *
from glslnodes import parser
from glslnodes.glsl.GLSLParser import GLSLParser
from glslnodes.glsl.GLSLParserListener import GLSLParserListener


# def test_enhanced0():
#     root = parser.load("./tests/examples/enhanced.0.frag")
#     assert (root)

class FragmentListener(GLSLParserListener):
    def __init__(self):
        pass

    def enterExternal_declaration(self, ctx:GLSLParser.External_declarationContext):
        print(ctx)


def test_sinewave():
    root = parser.load("./tests/examples/sinewave.frag")

    assert(root is not None)
    assert(len(root.variable_list.variable_list) == 6)
    # walker = ParseTreeWalker()
    # listener = FragmentListener()
    # walker.walk(listener, root)