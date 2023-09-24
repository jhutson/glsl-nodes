from glslnodes import parser
# from glslnodes.glsl import GLSLParser


def test_enhanced0():
    p = parser.load("./tests/examples/enhanced.0.frag")

    assert (p.translation_unit())