from glsl_compiler import parser
from glsl_compiler.glsl.GLSLParser import GLSLParser
from glsl_compiler.glsl.GLSLParserListener import GLSLParserListener


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
    assert(len(root.variable_list.variables) == 6)
    # walker = ParseTreeWalker()
    # listener = FragmentListener()
    # walker.walk(listener, root)