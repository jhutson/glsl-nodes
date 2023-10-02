# Generated from GLSLPreParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,307,243,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,1,0,5,0,70,8,0,10,0,12,0,73,9,0,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,88,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,
        12,5,12,127,8,12,10,12,12,12,130,9,12,1,13,1,13,1,13,1,13,1,13,5,
        13,137,8,13,10,13,12,13,140,9,13,1,13,3,13,143,8,13,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,5,14,152,8,14,10,14,12,14,155,9,14,1,14,3,
        14,158,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,5,15,167,8,15,10,
        15,12,15,170,9,15,1,15,3,15,173,8,15,1,15,1,15,1,16,1,16,1,16,1,
        16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,5,21,191,8,
        21,10,21,12,21,194,9,21,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,
        1,26,1,26,1,26,1,26,3,26,208,8,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,3,27,217,8,27,1,28,1,28,1,28,1,28,3,28,223,8,28,1,28,1,28,1,
        29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,
        33,3,33,241,8,33,1,33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,0,
        236,0,71,1,0,0,0,2,87,1,0,0,0,4,89,1,0,0,0,6,91,1,0,0,0,8,93,1,0,
        0,0,10,98,1,0,0,0,12,103,1,0,0,0,14,107,1,0,0,0,16,110,1,0,0,0,18,
        114,1,0,0,0,20,116,1,0,0,0,22,122,1,0,0,0,24,128,1,0,0,0,26,131,
        1,0,0,0,28,146,1,0,0,0,30,161,1,0,0,0,32,176,1,0,0,0,34,180,1,0,
        0,0,36,182,1,0,0,0,38,184,1,0,0,0,40,186,1,0,0,0,42,192,1,0,0,0,
        44,195,1,0,0,0,46,197,1,0,0,0,48,199,1,0,0,0,50,201,1,0,0,0,52,203,
        1,0,0,0,54,211,1,0,0,0,56,218,1,0,0,0,58,226,1,0,0,0,60,228,1,0,
        0,0,62,230,1,0,0,0,64,232,1,0,0,0,66,236,1,0,0,0,68,70,3,2,1,0,69,
        68,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,1,1,0,0,
        0,73,71,1,0,0,0,74,88,3,8,4,0,75,88,3,10,5,0,76,88,3,12,6,0,77,88,
        3,14,7,0,78,88,3,16,8,0,79,88,3,20,10,0,80,88,3,26,13,0,81,88,3,
        28,14,0,82,88,3,30,15,0,83,88,3,32,16,0,84,88,3,54,27,0,85,88,3,
        64,32,0,86,88,3,66,33,0,87,74,1,0,0,0,87,75,1,0,0,0,87,76,1,0,0,
        0,87,77,1,0,0,0,87,78,1,0,0,0,87,79,1,0,0,0,87,80,1,0,0,0,87,81,
        1,0,0,0,87,82,1,0,0,0,87,83,1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,0,
        87,86,1,0,0,0,88,3,1,0,0,0,89,90,5,281,0,0,90,5,1,0,0,0,91,92,5,
        277,0,0,92,7,1,0,0,0,93,94,5,230,0,0,94,95,5,259,0,0,95,96,3,40,
        20,0,96,97,3,42,21,0,97,9,1,0,0,0,98,99,5,230,0,0,99,100,5,260,0,
        0,100,101,3,6,3,0,101,102,3,24,12,0,102,11,1,0,0,0,103,104,5,230,
        0,0,104,105,5,261,0,0,105,106,3,24,12,0,106,13,1,0,0,0,107,108,5,
        230,0,0,108,109,5,262,0,0,109,15,1,0,0,0,110,111,5,230,0,0,111,112,
        5,263,0,0,112,113,3,18,9,0,113,17,1,0,0,0,114,115,5,279,0,0,115,
        19,1,0,0,0,116,117,5,230,0,0,117,118,5,264,0,0,118,119,3,22,11,0,
        119,120,5,210,0,0,120,121,3,4,2,0,121,21,1,0,0,0,122,123,5,282,0,
        0,123,23,1,0,0,0,124,127,3,60,30,0,125,127,3,2,1,0,126,124,1,0,0,
        0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,
        0,129,25,1,0,0,0,130,128,1,0,0,0,131,132,5,230,0,0,132,133,5,265,
        0,0,133,134,3,6,3,0,134,138,3,24,12,0,135,137,3,10,5,0,136,135,1,
        0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,142,1,
        0,0,0,140,138,1,0,0,0,141,143,3,12,6,0,142,141,1,0,0,0,142,143,1,
        0,0,0,143,144,1,0,0,0,144,145,3,14,7,0,145,27,1,0,0,0,146,147,5,
        230,0,0,147,148,5,266,0,0,148,149,3,38,19,0,149,153,3,24,12,0,150,
        152,3,10,5,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,
        154,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,156,158,3,12,6,0,157,
        156,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,3,14,7,0,160,
        29,1,0,0,0,161,162,5,230,0,0,162,163,5,267,0,0,163,164,3,38,19,0,
        164,168,3,24,12,0,165,167,3,10,5,0,166,165,1,0,0,0,167,170,1,0,0,
        0,168,166,1,0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,
        0,171,173,3,12,6,0,172,171,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,
        0,174,175,3,14,7,0,175,31,1,0,0,0,176,177,5,230,0,0,177,178,5,268,
        0,0,178,179,3,34,17,0,179,33,1,0,0,0,180,181,5,289,0,0,181,35,1,
        0,0,0,182,183,5,291,0,0,183,37,1,0,0,0,184,185,5,286,0,0,185,39,
        1,0,0,0,186,187,5,274,0,0,187,41,1,0,0,0,188,191,3,44,22,0,189,191,
        3,36,18,0,190,188,1,0,0,0,190,189,1,0,0,0,191,194,1,0,0,0,192,190,
        1,0,0,0,192,193,1,0,0,0,193,43,1,0,0,0,194,192,1,0,0,0,195,196,5,
        292,0,0,196,45,1,0,0,0,197,198,5,305,0,0,198,47,1,0,0,0,199,200,
        5,296,0,0,200,49,1,0,0,0,201,202,5,297,0,0,202,51,1,0,0,0,203,204,
        5,294,0,0,204,207,5,226,0,0,205,208,3,50,25,0,206,208,3,48,24,0,
        207,205,1,0,0,0,207,206,1,0,0,0,208,209,1,0,0,0,209,210,5,241,0,
        0,210,53,1,0,0,0,211,212,5,230,0,0,212,216,5,269,0,0,213,217,3,62,
        31,0,214,217,3,52,26,0,215,217,3,56,28,0,216,213,1,0,0,0,216,214,
        1,0,0,0,216,215,1,0,0,0,217,55,1,0,0,0,218,219,5,298,0,0,219,222,
        5,226,0,0,220,223,3,50,25,0,221,223,3,48,24,0,222,220,1,0,0,0,222,
        221,1,0,0,0,223,224,1,0,0,0,224,225,5,241,0,0,225,57,1,0,0,0,226,
        227,5,306,0,0,227,59,1,0,0,0,228,229,5,301,0,0,229,61,1,0,0,0,230,
        231,5,300,0,0,231,63,1,0,0,0,232,233,5,230,0,0,233,234,5,270,0,0,
        234,235,3,38,19,0,235,65,1,0,0,0,236,237,5,230,0,0,237,238,5,271,
        0,0,238,240,3,46,23,0,239,241,3,58,29,0,240,239,1,0,0,0,240,241,
        1,0,0,0,241,67,1,0,0,0,16,71,87,126,128,138,142,153,157,168,172,
        190,192,207,216,222,240
    ]

class GLSLPreParser ( Parser ):

    grammarFileName = "GLSLPreParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'atomic_uint'", "'attribute'", "'bool'", 
                     "'break'", "'buffer'", "'bvec2'", "'bvec3'", "'bvec4'", 
                     "'case'", "'centroid'", "'coherent'", "'const'", "'continue'", 
                     "'default'", "'discard'", "'dmat2'", "'dmat2x2'", "'dmat2x3'", 
                     "'dmat2x4'", "'dmat3'", "'dmat3x2'", "'dmat3x3'", "'dmat3x4'", 
                     "'dmat4'", "'dmat4x2'", "'dmat4x3'", "'dmat4x4'", "'do'", 
                     "'double'", "'dvec2'", "'dvec3'", "'dvec4'", "'else'", 
                     "'false'", "'flat'", "'float'", "'for'", "'highp'", 
                     "'if'", "'iimage1D'", "'iimage1DArray'", "'iimage2D'", 
                     "'iimage2DArray'", "'iimage2DMS'", "'iimage2DMSArray'", 
                     "'iimage2DRect'", "'iimage3D'", "'iimageBuffer'", "'iimageCube'", 
                     "'iimageCubeArray'", "'image1D'", "'image1DArray'", 
                     "'image2D'", "'image2DArray'", "'image2DMS'", "'image2DMSArray'", 
                     "'image2DRect'", "'image3D'", "'imageBuffer'", "'imageCube'", 
                     "'imageCubeArray'", "'in'", "'inout'", "'int'", "'invariant'", 
                     "'isampler1D'", "'isampler1DArray'", "'isampler2D'", 
                     "'isampler2DArray'", "'isampler2DMS'", "'isampler2DMSArray'", 
                     "'isampler2DRect'", "'isampler3D'", "'isamplerBuffer'", 
                     "'isamplerCube'", "'isamplerCubeArray'", "'isubpassInput'", 
                     "'isubpassInputMS'", "'itexture1D'", "'itexture1DArray'", 
                     "'itexture2D'", "'itexture2DArray'", "'itexture2DMS'", 
                     "'itexture2DMSArray'", "'itexture2DRect'", "'itexture3D'", 
                     "'itextureBuffer'", "'itextureCube'", "'itextureCubeArray'", 
                     "'ivec2'", "'ivec3'", "'ivec4'", "'layout'", "'lowp'", 
                     "'mat2'", "'mat2x2'", "'mat2x3'", "'mat2x4'", "'mat3'", 
                     "'mat3x2'", "'mat3x3'", "'mat3x4'", "'mat4'", "'mat4x2'", 
                     "'mat4x3'", "'mat4x4'", "'mediump'", "'noperspective'", 
                     "'out'", "'patch'", "'precise'", "'precision'", "'readonly'", 
                     "'restrict'", "'return'", "'sample'", "'sampler'", 
                     "'sampler1D'", "'sampler1DArray'", "'sampler1DArrayShadow'", 
                     "'sampler1DShadow'", "'sampler2D'", "'sampler2DArray'", 
                     "'sampler2DArrayShadow'", "'sampler2DMS'", "'sampler2DMSArray'", 
                     "'sampler2DRect'", "'sampler2DRectShadow'", "'sampler2DShadow'", 
                     "'sampler3D'", "'samplerBuffer'", "'samplerCube'", 
                     "'samplerCubeArray'", "'samplerCubeArrayShadow'", "'samplerCubeShadow'", 
                     "'samplerShadow'", "'shared'", "'smooth'", "'struct'", 
                     "'subpassInput'", "'subpassInputMS'", "'subroutine'", 
                     "'switch'", "'texture1D'", "'texture1DArray'", "'texture2D'", 
                     "'texture2DArray'", "'texture2DMS'", "'texture2DMSArray'", 
                     "'texture2DRect'", "'texture3D'", "'textureBuffer'", 
                     "'textureCube'", "'textureCubeArray'", "'true'", "'uimage1D'", 
                     "'uimage1DArray'", "'uimage2D'", "'uimage2DArray'", 
                     "'uimage2DMS'", "'uimage2DMSArray'", "'uimage2DRect'", 
                     "'uimage3D'", "'uimageBuffer'", "'uimageCube'", "'uimageCubeArray'", 
                     "'uint'", "'uniform'", "'usampler1D'", "'usampler1DArray'", 
                     "'usampler2D'", "'usampler2DArray'", "'usampler2DMS'", 
                     "'usampler2DMSArray'", "'usampler2DRect'", "'usampler3D'", 
                     "'usamplerBuffer'", "'usamplerCube'", "'usamplerCubeArray'", 
                     "'usubpassInput'", "'usubpassInputMS'", "'utexture1D'", 
                     "'utexture1DArray'", "'utexture2D'", "'utexture2DArray'", 
                     "'utexture2DMS'", "'utexture2DMSArray'", "'utexture2DRect'", 
                     "'utexture3D'", "'utextureBuffer'", "'utextureCube'", 
                     "'utextureCubeArray'", "'uvec2'", "'uvec3'", "'uvec4'", 
                     "'varying'", "'vec2'", "'vec3'", "'vec4'", "'void'", 
                     "'volatile'", "'while'", "'writeonly'", "'+='", "'&'", 
                     "'&='", "'&&'", "'!'", "'^'", "':'", "','", "'-'", 
                     "'--'", "'/='", "'.'", "'=='", "'='", "'>='", "'++'", 
                     "'<='", "'<'", "'<<='", "'{'", "'['", "'<<'", "'('", 
                     "'%='", "'*='", "'!='", "<INVALID>", "'|='", "'||'", 
                     "'%'", "'+'", "'?'", "'>'", "'>>='", "'}'", "']'", 
                     "'>>'", "')'", "';'", "'/'", "'*'", "'-='", "'~'", 
                     "'|'", "'^='", "'^^'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'debug'", "<INVALID>", "'off'", "'on'", 
                     "'optimize'", "<INVALID>", "'STDGL'" ]

    symbolicNames = [ "<INVALID>", "ATOMIC_UINT", "ATTRIBUTE", "BOOL", "BREAK", 
                      "BUFFER", "BVEC2", "BVEC3", "BVEC4", "CASE", "CENTROID", 
                      "COHERENT", "CONST", "CONTINUE", "DEFAULT", "DISCARD", 
                      "DMAT2", "DMAT2X2", "DMAT2X3", "DMAT2X4", "DMAT3", 
                      "DMAT3X2", "DMAT3X3", "DMAT3X4", "DMAT4", "DMAT4X2", 
                      "DMAT4X3", "DMAT4X4", "DO", "DOUBLE", "DVEC2", "DVEC3", 
                      "DVEC4", "ELSE", "FALSE", "FLAT", "FLOAT", "FOR", 
                      "HIGHP", "IF", "IIMAGE1D", "IIMAGE1DARRAY", "IIMAGE2D", 
                      "IIMAGE2DARRAY", "IIMAGE2DMS", "IIMAGE2DMSARRAY", 
                      "IIMAGE2DRECT", "IIMAGE3D", "IIMAGEBUFFER", "IIMAGECUBE", 
                      "IIMAGECUBEARRAY", "IMAGE1D", "IMAGE1DARRAY", "IMAGE2D", 
                      "IMAGE2DARRAY", "IMAGE2DMS", "IMAGE2DMSARRAY", "IMAGE2DRECT", 
                      "IMAGE3D", "IMAGEBUFFER", "IMAGECUBE", "IMAGECUBEARRAY", 
                      "IN", "INOUT", "INT", "INVARIANT", "ISAMPLER1D", "ISAMPLER1DARRAY", 
                      "ISAMPLER2D", "ISAMPLER2DARRAY", "ISAMPLER2DMS", "ISAMPLER2DMSARRAY", 
                      "ISAMPLER2DRECT", "ISAMPLER3D", "ISAMPLERBUFFER", 
                      "ISAMPLERCUBE", "ISAMPLERCUBEARRAY", "ISUBPASSINPUT", 
                      "ISUBPASSINPUTMS", "ITEXTURE1D", "ITEXTURE1DARRAY", 
                      "ITEXTURE2D", "ITEXTURE2DARRAY", "ITEXTURE2DMS", "ITEXTURE2DMSARRAY", 
                      "ITEXTURE2DRECT", "ITEXTURE3D", "ITEXTUREBUFFER", 
                      "ITEXTURECUBE", "ITEXTURECUBEARRAY", "IVEC2", "IVEC3", 
                      "IVEC4", "LAYOUT", "LOWP", "MAT2", "MAT2X2", "MAT2X3", 
                      "MAT2X4", "MAT3", "MAT3X2", "MAT3X3", "MAT3X4", "MAT4", 
                      "MAT4X2", "MAT4X3", "MAT4X4", "MEDIUMP", "NOPERSPECTIVE", 
                      "OUT", "PATCH", "PRECISE", "PRECISION", "READONLY", 
                      "RESTRICT", "RETURN", "SAMPLE", "SAMPLER", "SAMPLER1D", 
                      "SAMPLER1DARRAY", "SAMPLER1DARRAYSHADOW", "SAMPLER1DSHADOW", 
                      "SAMPLER2D", "SAMPLER2DARRAY", "SAMPLER2DARRAYSHADOW", 
                      "SAMPLER2DMS", "SAMPLER2DMSARRAY", "SAMPLER2DRECT", 
                      "SAMPLER2DRECTSHADOW", "SAMPLER2DSHADOW", "SAMPLER3D", 
                      "SAMPLERBUFFER", "SAMPLERCUBE", "SAMPLERCUBEARRAY", 
                      "SAMPLERCUBEARRAYSHADOW", "SAMPLERCUBESHADOW", "SAMPLERSHADOW", 
                      "SHARED", "SMOOTH", "STRUCT", "SUBPASSINPUT", "SUBPASSINPUTMS", 
                      "SUBROUTINE", "SWITCH", "TEXTURE1D", "TEXTURE1DARRAY", 
                      "TEXTURE2D", "TEXTURE2DARRAY", "TEXTURE2DMS", "TEXTURE2DMSARRAY", 
                      "TEXTURE2DRECT", "TEXTURE3D", "TEXTUREBUFFER", "TEXTURECUBE", 
                      "TEXTURECUBEARRAY", "TRUE", "UIMAGE1D", "UIMAGE1DARRAY", 
                      "UIMAGE2D", "UIMAGE2DARRAY", "UIMAGE2DMS", "UIMAGE2DMSARRAY", 
                      "UIMAGE2DRECT", "UIMAGE3D", "UIMAGEBUFFER", "UIMAGECUBE", 
                      "UIMAGECUBEARRAY", "UINT", "UNIFORM", "USAMPLER1D", 
                      "USAMPLER1DARRAY", "USAMPLER2D", "USAMPLER2DARRAY", 
                      "USAMPLER2DMS", "USAMPLER2DMSARRAY", "USAMPLER2DRECT", 
                      "USAMPLER3D", "USAMPLERBUFFER", "USAMPLERCUBE", "USAMPLERCUBEARRAY", 
                      "USUBPASSINPUT", "USUBPASSINPUTMS", "UTEXTURE1D", 
                      "UTEXTURE1DARRAY", "UTEXTURE2D", "UTEXTURE2DARRAY", 
                      "UTEXTURE2DMS", "UTEXTURE2DMSARRAY", "UTEXTURE2DRECT", 
                      "UTEXTURE3D", "UTEXTUREBUFFER", "UTEXTURECUBE", "UTEXTURECUBEARRAY", 
                      "UVEC2", "UVEC3", "UVEC4", "VARYING", "VEC2", "VEC3", 
                      "VEC4", "VOID", "VOLATILE", "WHILE", "WRITEONLY", 
                      "ADD_ASSIGN", "AMPERSAND", "AND_ASSIGN", "AND_OP", 
                      "BANG", "CARET", "COLON", "COMMA", "DASH", "DEC_OP", 
                      "DIV_ASSIGN", "DOT", "EQ_OP", "EQUAL", "GE_OP", "INC_OP", 
                      "LE_OP", "LEFT_ANGLE", "LEFT_ASSIGN", "LEFT_BRACE", 
                      "LEFT_BRACKET", "LEFT_OP", "LEFT_PAREN", "MOD_ASSIGN", 
                      "MUL_ASSIGN", "NE_OP", "NUMBER_SIGN", "OR_ASSIGN", 
                      "OR_OP", "PERCENT", "PLUS", "QUESTION", "RIGHT_ANGLE", 
                      "RIGHT_ASSIGN", "RIGHT_BRACE", "RIGHT_BRACKET", "RIGHT_OP", 
                      "RIGHT_PAREN", "SEMICOLON", "SLASH", "STAR", "SUB_ASSIGN", 
                      "TILDE", "VERTICAL_BAR", "XOR_ASSIGN", "XOR_OP", "DOUBLECONSTANT", 
                      "FLOATCONSTANT", "INTCONSTANT", "UINTCONSTANT", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "LINE_CONTINUATION", "IDENTIFIER", 
                      "WHITE_SPACE", "DEFINE_DIRECTIVE", "ELIF_DIRECTIVE", 
                      "ELSE_DIRECTIVE", "ENDIF_DIRECTIVE", "ERROR_DIRECTIVE", 
                      "EXTENSION_DIRECTIVE", "IF_DIRECTIVE", "IFDEF_DIRECTIVE", 
                      "IFNDEF_DIRECTIVE", "LINE_DIRECTIVE", "PRAGMA_DIRECTIVE", 
                      "UNDEF_DIRECTIVE", "VERSION_DIRECTIVE", "SPACE_TAB_0", 
                      "NEWLINE_0", "MACRO_NAME", "NEWLINE_1", "SPACE_TAB_1", 
                      "CONSTANT_EXPRESSION", "NEWLINE_2", "ERROR_MESSAGE", 
                      "NEWLINE_3", "BEHAVIOR", "EXTENSION_NAME", "NEWLINE_4", 
                      "SPACE_TAB_2", "NEWLINE_5", "MACRO_IDENTIFIER", "NEWLINE_6", 
                      "SPACE_TAB_3", "LINE_EXPRESSION", "NEWLINE_7", "MACRO_ESC_NEWLINE", 
                      "MACRO_TEXT", "NEWLINE_8", "DEBUG", "NEWLINE_9", "OFF", 
                      "ON", "OPTIMIZE", "SPACE_TAB_5", "STDGL", "PROGRAM_TEXT", 
                      "NEWLINE_10", "SPACE_TAB_6", "NEWLINE_11", "NUMBER", 
                      "PROFILE", "SPACE_TAB_7" ]

    RULE_translation_unit = 0
    RULE_compiler_directive = 1
    RULE_behavior = 2
    RULE_constant_expression = 3
    RULE_define_directive = 4
    RULE_elif_directive = 5
    RULE_else_directive = 6
    RULE_endif_directive = 7
    RULE_error_directive = 8
    RULE_error_message = 9
    RULE_extension_directive = 10
    RULE_extension_name = 11
    RULE_group_of_lines = 12
    RULE_if_directive = 13
    RULE_ifdef_directive = 14
    RULE_ifndef_directive = 15
    RULE_line_directive = 16
    RULE_line_expression = 17
    RULE_macro_esc_newline = 18
    RULE_macro_identifier = 19
    RULE_macro_name = 20
    RULE_macro_text = 21
    RULE_macro_text_ = 22
    RULE_number = 23
    RULE_off = 24
    RULE_on = 25
    RULE_pragma_debug = 26
    RULE_pragma_directive = 27
    RULE_pragma_optimize = 28
    RULE_profile = 29
    RULE_program_text = 30
    RULE_stdgl = 31
    RULE_undef_directive = 32
    RULE_version_directive = 33

    ruleNames =  [ "translation_unit", "compiler_directive", "behavior", 
                   "constant_expression", "define_directive", "elif_directive", 
                   "else_directive", "endif_directive", "error_directive", 
                   "error_message", "extension_directive", "extension_name", 
                   "group_of_lines", "if_directive", "ifdef_directive", 
                   "ifndef_directive", "line_directive", "line_expression", 
                   "macro_esc_newline", "macro_identifier", "macro_name", 
                   "macro_text", "macro_text_", "number", "off", "on", "pragma_debug", 
                   "pragma_directive", "pragma_optimize", "profile", "program_text", 
                   "stdgl", "undef_directive", "version_directive" ]

    EOF = Token.EOF
    ATOMIC_UINT=1
    ATTRIBUTE=2
    BOOL=3
    BREAK=4
    BUFFER=5
    BVEC2=6
    BVEC3=7
    BVEC4=8
    CASE=9
    CENTROID=10
    COHERENT=11
    CONST=12
    CONTINUE=13
    DEFAULT=14
    DISCARD=15
    DMAT2=16
    DMAT2X2=17
    DMAT2X3=18
    DMAT2X4=19
    DMAT3=20
    DMAT3X2=21
    DMAT3X3=22
    DMAT3X4=23
    DMAT4=24
    DMAT4X2=25
    DMAT4X3=26
    DMAT4X4=27
    DO=28
    DOUBLE=29
    DVEC2=30
    DVEC3=31
    DVEC4=32
    ELSE=33
    FALSE=34
    FLAT=35
    FLOAT=36
    FOR=37
    HIGHP=38
    IF=39
    IIMAGE1D=40
    IIMAGE1DARRAY=41
    IIMAGE2D=42
    IIMAGE2DARRAY=43
    IIMAGE2DMS=44
    IIMAGE2DMSARRAY=45
    IIMAGE2DRECT=46
    IIMAGE3D=47
    IIMAGEBUFFER=48
    IIMAGECUBE=49
    IIMAGECUBEARRAY=50
    IMAGE1D=51
    IMAGE1DARRAY=52
    IMAGE2D=53
    IMAGE2DARRAY=54
    IMAGE2DMS=55
    IMAGE2DMSARRAY=56
    IMAGE2DRECT=57
    IMAGE3D=58
    IMAGEBUFFER=59
    IMAGECUBE=60
    IMAGECUBEARRAY=61
    IN=62
    INOUT=63
    INT=64
    INVARIANT=65
    ISAMPLER1D=66
    ISAMPLER1DARRAY=67
    ISAMPLER2D=68
    ISAMPLER2DARRAY=69
    ISAMPLER2DMS=70
    ISAMPLER2DMSARRAY=71
    ISAMPLER2DRECT=72
    ISAMPLER3D=73
    ISAMPLERBUFFER=74
    ISAMPLERCUBE=75
    ISAMPLERCUBEARRAY=76
    ISUBPASSINPUT=77
    ISUBPASSINPUTMS=78
    ITEXTURE1D=79
    ITEXTURE1DARRAY=80
    ITEXTURE2D=81
    ITEXTURE2DARRAY=82
    ITEXTURE2DMS=83
    ITEXTURE2DMSARRAY=84
    ITEXTURE2DRECT=85
    ITEXTURE3D=86
    ITEXTUREBUFFER=87
    ITEXTURECUBE=88
    ITEXTURECUBEARRAY=89
    IVEC2=90
    IVEC3=91
    IVEC4=92
    LAYOUT=93
    LOWP=94
    MAT2=95
    MAT2X2=96
    MAT2X3=97
    MAT2X4=98
    MAT3=99
    MAT3X2=100
    MAT3X3=101
    MAT3X4=102
    MAT4=103
    MAT4X2=104
    MAT4X3=105
    MAT4X4=106
    MEDIUMP=107
    NOPERSPECTIVE=108
    OUT=109
    PATCH=110
    PRECISE=111
    PRECISION=112
    READONLY=113
    RESTRICT=114
    RETURN=115
    SAMPLE=116
    SAMPLER=117
    SAMPLER1D=118
    SAMPLER1DARRAY=119
    SAMPLER1DARRAYSHADOW=120
    SAMPLER1DSHADOW=121
    SAMPLER2D=122
    SAMPLER2DARRAY=123
    SAMPLER2DARRAYSHADOW=124
    SAMPLER2DMS=125
    SAMPLER2DMSARRAY=126
    SAMPLER2DRECT=127
    SAMPLER2DRECTSHADOW=128
    SAMPLER2DSHADOW=129
    SAMPLER3D=130
    SAMPLERBUFFER=131
    SAMPLERCUBE=132
    SAMPLERCUBEARRAY=133
    SAMPLERCUBEARRAYSHADOW=134
    SAMPLERCUBESHADOW=135
    SAMPLERSHADOW=136
    SHARED=137
    SMOOTH=138
    STRUCT=139
    SUBPASSINPUT=140
    SUBPASSINPUTMS=141
    SUBROUTINE=142
    SWITCH=143
    TEXTURE1D=144
    TEXTURE1DARRAY=145
    TEXTURE2D=146
    TEXTURE2DARRAY=147
    TEXTURE2DMS=148
    TEXTURE2DMSARRAY=149
    TEXTURE2DRECT=150
    TEXTURE3D=151
    TEXTUREBUFFER=152
    TEXTURECUBE=153
    TEXTURECUBEARRAY=154
    TRUE=155
    UIMAGE1D=156
    UIMAGE1DARRAY=157
    UIMAGE2D=158
    UIMAGE2DARRAY=159
    UIMAGE2DMS=160
    UIMAGE2DMSARRAY=161
    UIMAGE2DRECT=162
    UIMAGE3D=163
    UIMAGEBUFFER=164
    UIMAGECUBE=165
    UIMAGECUBEARRAY=166
    UINT=167
    UNIFORM=168
    USAMPLER1D=169
    USAMPLER1DARRAY=170
    USAMPLER2D=171
    USAMPLER2DARRAY=172
    USAMPLER2DMS=173
    USAMPLER2DMSARRAY=174
    USAMPLER2DRECT=175
    USAMPLER3D=176
    USAMPLERBUFFER=177
    USAMPLERCUBE=178
    USAMPLERCUBEARRAY=179
    USUBPASSINPUT=180
    USUBPASSINPUTMS=181
    UTEXTURE1D=182
    UTEXTURE1DARRAY=183
    UTEXTURE2D=184
    UTEXTURE2DARRAY=185
    UTEXTURE2DMS=186
    UTEXTURE2DMSARRAY=187
    UTEXTURE2DRECT=188
    UTEXTURE3D=189
    UTEXTUREBUFFER=190
    UTEXTURECUBE=191
    UTEXTURECUBEARRAY=192
    UVEC2=193
    UVEC3=194
    UVEC4=195
    VARYING=196
    VEC2=197
    VEC3=198
    VEC4=199
    VOID=200
    VOLATILE=201
    WHILE=202
    WRITEONLY=203
    ADD_ASSIGN=204
    AMPERSAND=205
    AND_ASSIGN=206
    AND_OP=207
    BANG=208
    CARET=209
    COLON=210
    COMMA=211
    DASH=212
    DEC_OP=213
    DIV_ASSIGN=214
    DOT=215
    EQ_OP=216
    EQUAL=217
    GE_OP=218
    INC_OP=219
    LE_OP=220
    LEFT_ANGLE=221
    LEFT_ASSIGN=222
    LEFT_BRACE=223
    LEFT_BRACKET=224
    LEFT_OP=225
    LEFT_PAREN=226
    MOD_ASSIGN=227
    MUL_ASSIGN=228
    NE_OP=229
    NUMBER_SIGN=230
    OR_ASSIGN=231
    OR_OP=232
    PERCENT=233
    PLUS=234
    QUESTION=235
    RIGHT_ANGLE=236
    RIGHT_ASSIGN=237
    RIGHT_BRACE=238
    RIGHT_BRACKET=239
    RIGHT_OP=240
    RIGHT_PAREN=241
    SEMICOLON=242
    SLASH=243
    STAR=244
    SUB_ASSIGN=245
    TILDE=246
    VERTICAL_BAR=247
    XOR_ASSIGN=248
    XOR_OP=249
    DOUBLECONSTANT=250
    FLOATCONSTANT=251
    INTCONSTANT=252
    UINTCONSTANT=253
    BLOCK_COMMENT=254
    LINE_COMMENT=255
    LINE_CONTINUATION=256
    IDENTIFIER=257
    WHITE_SPACE=258
    DEFINE_DIRECTIVE=259
    ELIF_DIRECTIVE=260
    ELSE_DIRECTIVE=261
    ENDIF_DIRECTIVE=262
    ERROR_DIRECTIVE=263
    EXTENSION_DIRECTIVE=264
    IF_DIRECTIVE=265
    IFDEF_DIRECTIVE=266
    IFNDEF_DIRECTIVE=267
    LINE_DIRECTIVE=268
    PRAGMA_DIRECTIVE=269
    UNDEF_DIRECTIVE=270
    VERSION_DIRECTIVE=271
    SPACE_TAB_0=272
    NEWLINE_0=273
    MACRO_NAME=274
    NEWLINE_1=275
    SPACE_TAB_1=276
    CONSTANT_EXPRESSION=277
    NEWLINE_2=278
    ERROR_MESSAGE=279
    NEWLINE_3=280
    BEHAVIOR=281
    EXTENSION_NAME=282
    NEWLINE_4=283
    SPACE_TAB_2=284
    NEWLINE_5=285
    MACRO_IDENTIFIER=286
    NEWLINE_6=287
    SPACE_TAB_3=288
    LINE_EXPRESSION=289
    NEWLINE_7=290
    MACRO_ESC_NEWLINE=291
    MACRO_TEXT=292
    NEWLINE_8=293
    DEBUG=294
    NEWLINE_9=295
    OFF=296
    ON=297
    OPTIMIZE=298
    SPACE_TAB_5=299
    STDGL=300
    PROGRAM_TEXT=301
    NEWLINE_10=302
    SPACE_TAB_6=303
    NEWLINE_11=304
    NUMBER=305
    PROFILE=306
    SPACE_TAB_7=307

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Translation_unitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compiler_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Compiler_directiveContext)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Compiler_directiveContext,i)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_translation_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslation_unit" ):
                listener.enterTranslation_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslation_unit" ):
                listener.exitTranslation_unit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranslation_unit" ):
                return visitor.visitTranslation_unit(self)
            else:
                return visitor.visitChildren(self)




    def translation_unit(self):

        localctx = GLSLPreParser.Translation_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_translation_unit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==230:
                self.state = 68
                self.compiler_directive()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compiler_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def define_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Define_directiveContext,0)


        def elif_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Elif_directiveContext,0)


        def else_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Else_directiveContext,0)


        def endif_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Endif_directiveContext,0)


        def error_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Error_directiveContext,0)


        def extension_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Extension_directiveContext,0)


        def if_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.If_directiveContext,0)


        def ifdef_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Ifdef_directiveContext,0)


        def ifndef_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Ifndef_directiveContext,0)


        def line_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Line_directiveContext,0)


        def pragma_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Pragma_directiveContext,0)


        def undef_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Undef_directiveContext,0)


        def version_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Version_directiveContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_compiler_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompiler_directive" ):
                listener.enterCompiler_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompiler_directive" ):
                listener.exitCompiler_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompiler_directive" ):
                return visitor.visitCompiler_directive(self)
            else:
                return visitor.visitChildren(self)




    def compiler_directive(self):

        localctx = GLSLPreParser.Compiler_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_compiler_directive)
        try:
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.define_directive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.elif_directive()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.else_directive()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.endif_directive()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.error_directive()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.extension_directive()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.if_directive()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 81
                self.ifdef_directive()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 82
                self.ifndef_directive()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 83
                self.line_directive()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 84
                self.pragma_directive()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 85
                self.undef_directive()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 86
                self.version_directive()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BehaviorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEHAVIOR(self):
            return self.getToken(GLSLPreParser.BEHAVIOR, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_behavior

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBehavior" ):
                listener.enterBehavior(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBehavior" ):
                listener.exitBehavior(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBehavior" ):
                return visitor.visitBehavior(self)
            else:
                return visitor.visitChildren(self)




    def behavior(self):

        localctx = GLSLPreParser.BehaviorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_behavior)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(GLSLPreParser.BEHAVIOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANT_EXPRESSION(self):
            return self.getToken(GLSLPreParser.CONSTANT_EXPRESSION, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_constant_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant_expression" ):
                listener.enterConstant_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant_expression" ):
                listener.exitConstant_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_expression" ):
                return visitor.visitConstant_expression(self)
            else:
                return visitor.visitChildren(self)




    def constant_expression(self):

        localctx = GLSLPreParser.Constant_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constant_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(GLSLPreParser.CONSTANT_EXPRESSION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Define_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def DEFINE_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.DEFINE_DIRECTIVE, 0)

        def macro_name(self):
            return self.getTypedRuleContext(GLSLPreParser.Macro_nameContext,0)


        def macro_text(self):
            return self.getTypedRuleContext(GLSLPreParser.Macro_textContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_define_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefine_directive" ):
                listener.enterDefine_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefine_directive" ):
                listener.exitDefine_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefine_directive" ):
                return visitor.visitDefine_directive(self)
            else:
                return visitor.visitChildren(self)




    def define_directive(self):

        localctx = GLSLPreParser.Define_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_define_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 94
            self.match(GLSLPreParser.DEFINE_DIRECTIVE)
            self.state = 95
            self.macro_name()
            self.state = 96
            self.macro_text()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def ELIF_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.ELIF_DIRECTIVE, 0)

        def constant_expression(self):
            return self.getTypedRuleContext(GLSLPreParser.Constant_expressionContext,0)


        def group_of_lines(self):
            return self.getTypedRuleContext(GLSLPreParser.Group_of_linesContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_elif_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_directive" ):
                listener.enterElif_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_directive" ):
                listener.exitElif_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_directive" ):
                return visitor.visitElif_directive(self)
            else:
                return visitor.visitChildren(self)




    def elif_directive(self):

        localctx = GLSLPreParser.Elif_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elif_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 99
            self.match(GLSLPreParser.ELIF_DIRECTIVE)
            self.state = 100
            self.constant_expression()
            self.state = 101
            self.group_of_lines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def ELSE_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.ELSE_DIRECTIVE, 0)

        def group_of_lines(self):
            return self.getTypedRuleContext(GLSLPreParser.Group_of_linesContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_else_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_directive" ):
                listener.enterElse_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_directive" ):
                listener.exitElse_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_directive" ):
                return visitor.visitElse_directive(self)
            else:
                return visitor.visitChildren(self)




    def else_directive(self):

        localctx = GLSLPreParser.Else_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_else_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 104
            self.match(GLSLPreParser.ELSE_DIRECTIVE)
            self.state = 105
            self.group_of_lines()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Endif_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def ENDIF_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.ENDIF_DIRECTIVE, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_endif_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndif_directive" ):
                listener.enterEndif_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndif_directive" ):
                listener.exitEndif_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEndif_directive" ):
                return visitor.visitEndif_directive(self)
            else:
                return visitor.visitChildren(self)




    def endif_directive(self):

        localctx = GLSLPreParser.Endif_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_endif_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 108
            self.match(GLSLPreParser.ENDIF_DIRECTIVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Error_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def ERROR_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.ERROR_DIRECTIVE, 0)

        def error_message(self):
            return self.getTypedRuleContext(GLSLPreParser.Error_messageContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_error_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterError_directive" ):
                listener.enterError_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitError_directive" ):
                listener.exitError_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitError_directive" ):
                return visitor.visitError_directive(self)
            else:
                return visitor.visitChildren(self)




    def error_directive(self):

        localctx = GLSLPreParser.Error_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_error_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 111
            self.match(GLSLPreParser.ERROR_DIRECTIVE)
            self.state = 112
            self.error_message()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Error_messageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ERROR_MESSAGE(self):
            return self.getToken(GLSLPreParser.ERROR_MESSAGE, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_error_message

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterError_message" ):
                listener.enterError_message(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitError_message" ):
                listener.exitError_message(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitError_message" ):
                return visitor.visitError_message(self)
            else:
                return visitor.visitChildren(self)




    def error_message(self):

        localctx = GLSLPreParser.Error_messageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_error_message)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(GLSLPreParser.ERROR_MESSAGE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extension_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def EXTENSION_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.EXTENSION_DIRECTIVE, 0)

        def extension_name(self):
            return self.getTypedRuleContext(GLSLPreParser.Extension_nameContext,0)


        def COLON(self):
            return self.getToken(GLSLPreParser.COLON, 0)

        def behavior(self):
            return self.getTypedRuleContext(GLSLPreParser.BehaviorContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_extension_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension_directive" ):
                listener.enterExtension_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension_directive" ):
                listener.exitExtension_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtension_directive" ):
                return visitor.visitExtension_directive(self)
            else:
                return visitor.visitChildren(self)




    def extension_directive(self):

        localctx = GLSLPreParser.Extension_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_extension_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 117
            self.match(GLSLPreParser.EXTENSION_DIRECTIVE)
            self.state = 118
            self.extension_name()
            self.state = 119
            self.match(GLSLPreParser.COLON)
            self.state = 120
            self.behavior()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Extension_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENSION_NAME(self):
            return self.getToken(GLSLPreParser.EXTENSION_NAME, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_extension_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension_name" ):
                listener.enterExtension_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension_name" ):
                listener.exitExtension_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtension_name" ):
                return visitor.visitExtension_name(self)
            else:
                return visitor.visitChildren(self)




    def extension_name(self):

        localctx = GLSLPreParser.Extension_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_extension_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(GLSLPreParser.EXTENSION_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_of_linesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_text(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Program_textContext)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Program_textContext,i)


        def compiler_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Compiler_directiveContext)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Compiler_directiveContext,i)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_group_of_lines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_of_lines" ):
                listener.enterGroup_of_lines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_of_lines" ):
                listener.exitGroup_of_lines(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup_of_lines" ):
                return visitor.visitGroup_of_lines(self)
            else:
                return visitor.visitChildren(self)




    def group_of_lines(self):

        localctx = GLSLPreParser.Group_of_linesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_group_of_lines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 126
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [301]:
                        self.state = 124
                        self.program_text()
                        pass
                    elif token in [230]:
                        self.state = 125
                        self.compiler_directive()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def IF_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.IF_DIRECTIVE, 0)

        def constant_expression(self):
            return self.getTypedRuleContext(GLSLPreParser.Constant_expressionContext,0)


        def group_of_lines(self):
            return self.getTypedRuleContext(GLSLPreParser.Group_of_linesContext,0)


        def endif_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Endif_directiveContext,0)


        def elif_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Elif_directiveContext)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Elif_directiveContext,i)


        def else_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Else_directiveContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_if_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_directive" ):
                listener.enterIf_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_directive" ):
                listener.exitIf_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_directive" ):
                return visitor.visitIf_directive(self)
            else:
                return visitor.visitChildren(self)




    def if_directive(self):

        localctx = GLSLPreParser.If_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_if_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 132
            self.match(GLSLPreParser.IF_DIRECTIVE)
            self.state = 133
            self.constant_expression()
            self.state = 134
            self.group_of_lines()
            self.state = 138
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 135
                    self.elif_directive() 
                self.state = 140
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 141
                self.else_directive()


            self.state = 144
            self.endif_directive()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifdef_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def IFDEF_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.IFDEF_DIRECTIVE, 0)

        def macro_identifier(self):
            return self.getTypedRuleContext(GLSLPreParser.Macro_identifierContext,0)


        def group_of_lines(self):
            return self.getTypedRuleContext(GLSLPreParser.Group_of_linesContext,0)


        def endif_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Endif_directiveContext,0)


        def elif_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Elif_directiveContext)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Elif_directiveContext,i)


        def else_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Else_directiveContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_ifdef_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfdef_directive" ):
                listener.enterIfdef_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfdef_directive" ):
                listener.exitIfdef_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfdef_directive" ):
                return visitor.visitIfdef_directive(self)
            else:
                return visitor.visitChildren(self)




    def ifdef_directive(self):

        localctx = GLSLPreParser.Ifdef_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifdef_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 147
            self.match(GLSLPreParser.IFDEF_DIRECTIVE)
            self.state = 148
            self.macro_identifier()
            self.state = 149
            self.group_of_lines()
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 150
                    self.elif_directive() 
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 156
                self.else_directive()


            self.state = 159
            self.endif_directive()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ifndef_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def IFNDEF_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.IFNDEF_DIRECTIVE, 0)

        def macro_identifier(self):
            return self.getTypedRuleContext(GLSLPreParser.Macro_identifierContext,0)


        def group_of_lines(self):
            return self.getTypedRuleContext(GLSLPreParser.Group_of_linesContext,0)


        def endif_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Endif_directiveContext,0)


        def elif_directive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Elif_directiveContext)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Elif_directiveContext,i)


        def else_directive(self):
            return self.getTypedRuleContext(GLSLPreParser.Else_directiveContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_ifndef_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfndef_directive" ):
                listener.enterIfndef_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfndef_directive" ):
                listener.exitIfndef_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfndef_directive" ):
                return visitor.visitIfndef_directive(self)
            else:
                return visitor.visitChildren(self)




    def ifndef_directive(self):

        localctx = GLSLPreParser.Ifndef_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_ifndef_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 162
            self.match(GLSLPreParser.IFNDEF_DIRECTIVE)
            self.state = 163
            self.macro_identifier()
            self.state = 164
            self.group_of_lines()
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.elif_directive() 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 171
                self.else_directive()


            self.state = 174
            self.endif_directive()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def LINE_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.LINE_DIRECTIVE, 0)

        def line_expression(self):
            return self.getTypedRuleContext(GLSLPreParser.Line_expressionContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_line_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_directive" ):
                listener.enterLine_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_directive" ):
                listener.exitLine_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_directive" ):
                return visitor.visitLine_directive(self)
            else:
                return visitor.visitChildren(self)




    def line_directive(self):

        localctx = GLSLPreParser.Line_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_line_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 177
            self.match(GLSLPreParser.LINE_DIRECTIVE)
            self.state = 178
            self.line_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINE_EXPRESSION(self):
            return self.getToken(GLSLPreParser.LINE_EXPRESSION, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_line_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_expression" ):
                listener.enterLine_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_expression" ):
                listener.exitLine_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_expression" ):
                return visitor.visitLine_expression(self)
            else:
                return visitor.visitChildren(self)




    def line_expression(self):

        localctx = GLSLPreParser.Line_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_line_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(GLSLPreParser.LINE_EXPRESSION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_esc_newlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_ESC_NEWLINE(self):
            return self.getToken(GLSLPreParser.MACRO_ESC_NEWLINE, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_macro_esc_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_esc_newline" ):
                listener.enterMacro_esc_newline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_esc_newline" ):
                listener.exitMacro_esc_newline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_esc_newline" ):
                return visitor.visitMacro_esc_newline(self)
            else:
                return visitor.visitChildren(self)




    def macro_esc_newline(self):

        localctx = GLSLPreParser.Macro_esc_newlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_macro_esc_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(GLSLPreParser.MACRO_ESC_NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_IDENTIFIER(self):
            return self.getToken(GLSLPreParser.MACRO_IDENTIFIER, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_macro_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_identifier" ):
                listener.enterMacro_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_identifier" ):
                listener.exitMacro_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_identifier" ):
                return visitor.visitMacro_identifier(self)
            else:
                return visitor.visitChildren(self)




    def macro_identifier(self):

        localctx = GLSLPreParser.Macro_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_macro_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(GLSLPreParser.MACRO_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_NAME(self):
            return self.getToken(GLSLPreParser.MACRO_NAME, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_macro_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_name" ):
                listener.enterMacro_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_name" ):
                listener.exitMacro_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_name" ):
                return visitor.visitMacro_name(self)
            else:
                return visitor.visitChildren(self)




    def macro_name(self):

        localctx = GLSLPreParser.Macro_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_macro_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(GLSLPreParser.MACRO_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def macro_text_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Macro_text_Context)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Macro_text_Context,i)


        def macro_esc_newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GLSLPreParser.Macro_esc_newlineContext)
            else:
                return self.getTypedRuleContext(GLSLPreParser.Macro_esc_newlineContext,i)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_macro_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_text" ):
                listener.enterMacro_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_text" ):
                listener.exitMacro_text(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_text" ):
                return visitor.visitMacro_text(self)
            else:
                return visitor.visitChildren(self)




    def macro_text(self):

        localctx = GLSLPreParser.Macro_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_macro_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==291 or _la==292:
                self.state = 190
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [292]:
                    self.state = 188
                    self.macro_text_()
                    pass
                elif token in [291]:
                    self.state = 189
                    self.macro_esc_newline()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_text_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_TEXT(self):
            return self.getToken(GLSLPreParser.MACRO_TEXT, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_macro_text_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_text_" ):
                listener.enterMacro_text_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_text_" ):
                listener.exitMacro_text_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_text_" ):
                return visitor.visitMacro_text_(self)
            else:
                return visitor.visitChildren(self)




    def macro_text_(self):

        localctx = GLSLPreParser.Macro_text_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_macro_text_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(GLSLPreParser.MACRO_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(GLSLPreParser.NUMBER, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = GLSLPreParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(GLSLPreParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OFF(self):
            return self.getToken(GLSLPreParser.OFF, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_off

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOff" ):
                listener.enterOff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOff" ):
                listener.exitOff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOff" ):
                return visitor.visitOff(self)
            else:
                return visitor.visitChildren(self)




    def off(self):

        localctx = GLSLPreParser.OffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_off)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(GLSLPreParser.OFF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(GLSLPreParser.ON, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_on

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn" ):
                listener.enterOn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn" ):
                listener.exitOn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn" ):
                return visitor.visitOn(self)
            else:
                return visitor.visitChildren(self)




    def on(self):

        localctx = GLSLPreParser.OnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_on)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(GLSLPreParser.ON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_debugContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEBUG(self):
            return self.getToken(GLSLPreParser.DEBUG, 0)

        def LEFT_PAREN(self):
            return self.getToken(GLSLPreParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(GLSLPreParser.RIGHT_PAREN, 0)

        def on(self):
            return self.getTypedRuleContext(GLSLPreParser.OnContext,0)


        def off(self):
            return self.getTypedRuleContext(GLSLPreParser.OffContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_pragma_debug

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_debug" ):
                listener.enterPragma_debug(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_debug" ):
                listener.exitPragma_debug(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_debug" ):
                return visitor.visitPragma_debug(self)
            else:
                return visitor.visitChildren(self)




    def pragma_debug(self):

        localctx = GLSLPreParser.Pragma_debugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_pragma_debug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(GLSLPreParser.DEBUG)
            self.state = 204
            self.match(GLSLPreParser.LEFT_PAREN)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [297]:
                self.state = 205
                self.on()
                pass
            elif token in [296]:
                self.state = 206
                self.off()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 209
            self.match(GLSLPreParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def PRAGMA_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.PRAGMA_DIRECTIVE, 0)

        def stdgl(self):
            return self.getTypedRuleContext(GLSLPreParser.StdglContext,0)


        def pragma_debug(self):
            return self.getTypedRuleContext(GLSLPreParser.Pragma_debugContext,0)


        def pragma_optimize(self):
            return self.getTypedRuleContext(GLSLPreParser.Pragma_optimizeContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_pragma_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_directive" ):
                listener.enterPragma_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_directive" ):
                listener.exitPragma_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_directive" ):
                return visitor.visitPragma_directive(self)
            else:
                return visitor.visitChildren(self)




    def pragma_directive(self):

        localctx = GLSLPreParser.Pragma_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_pragma_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 212
            self.match(GLSLPreParser.PRAGMA_DIRECTIVE)
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [300]:
                self.state = 213
                self.stdgl()
                pass
            elif token in [294]:
                self.state = 214
                self.pragma_debug()
                pass
            elif token in [298]:
                self.state = 215
                self.pragma_optimize()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_optimizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIMIZE(self):
            return self.getToken(GLSLPreParser.OPTIMIZE, 0)

        def LEFT_PAREN(self):
            return self.getToken(GLSLPreParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(GLSLPreParser.RIGHT_PAREN, 0)

        def on(self):
            return self.getTypedRuleContext(GLSLPreParser.OnContext,0)


        def off(self):
            return self.getTypedRuleContext(GLSLPreParser.OffContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_pragma_optimize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_optimize" ):
                listener.enterPragma_optimize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_optimize" ):
                listener.exitPragma_optimize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPragma_optimize" ):
                return visitor.visitPragma_optimize(self)
            else:
                return visitor.visitChildren(self)




    def pragma_optimize(self):

        localctx = GLSLPreParser.Pragma_optimizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_pragma_optimize)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(GLSLPreParser.OPTIMIZE)
            self.state = 219
            self.match(GLSLPreParser.LEFT_PAREN)
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [297]:
                self.state = 220
                self.on()
                pass
            elif token in [296]:
                self.state = 221
                self.off()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 224
            self.match(GLSLPreParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProfileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROFILE(self):
            return self.getToken(GLSLPreParser.PROFILE, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_profile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProfile" ):
                listener.enterProfile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProfile" ):
                listener.exitProfile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProfile" ):
                return visitor.visitProfile(self)
            else:
                return visitor.visitChildren(self)




    def profile(self):

        localctx = GLSLPreParser.ProfileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_profile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(GLSLPreParser.PROFILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM_TEXT(self):
            return self.getToken(GLSLPreParser.PROGRAM_TEXT, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_program_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_text" ):
                listener.enterProgram_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_text" ):
                listener.exitProgram_text(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_text" ):
                return visitor.visitProgram_text(self)
            else:
                return visitor.visitChildren(self)




    def program_text(self):

        localctx = GLSLPreParser.Program_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_program_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(GLSLPreParser.PROGRAM_TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StdglContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STDGL(self):
            return self.getToken(GLSLPreParser.STDGL, 0)

        def getRuleIndex(self):
            return GLSLPreParser.RULE_stdgl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStdgl" ):
                listener.enterStdgl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStdgl" ):
                listener.exitStdgl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStdgl" ):
                return visitor.visitStdgl(self)
            else:
                return visitor.visitChildren(self)




    def stdgl(self):

        localctx = GLSLPreParser.StdglContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stdgl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(GLSLPreParser.STDGL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Undef_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def UNDEF_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.UNDEF_DIRECTIVE, 0)

        def macro_identifier(self):
            return self.getTypedRuleContext(GLSLPreParser.Macro_identifierContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_undef_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUndef_directive" ):
                listener.enterUndef_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUndef_directive" ):
                listener.exitUndef_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUndef_directive" ):
                return visitor.visitUndef_directive(self)
            else:
                return visitor.visitChildren(self)




    def undef_directive(self):

        localctx = GLSLPreParser.Undef_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_undef_directive)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 233
            self.match(GLSLPreParser.UNDEF_DIRECTIVE)
            self.state = 234
            self.macro_identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Version_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_SIGN(self):
            return self.getToken(GLSLPreParser.NUMBER_SIGN, 0)

        def VERSION_DIRECTIVE(self):
            return self.getToken(GLSLPreParser.VERSION_DIRECTIVE, 0)

        def number(self):
            return self.getTypedRuleContext(GLSLPreParser.NumberContext,0)


        def profile(self):
            return self.getTypedRuleContext(GLSLPreParser.ProfileContext,0)


        def getRuleIndex(self):
            return GLSLPreParser.RULE_version_directive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersion_directive" ):
                listener.enterVersion_directive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersion_directive" ):
                listener.exitVersion_directive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion_directive" ):
                return visitor.visitVersion_directive(self)
            else:
                return visitor.visitChildren(self)




    def version_directive(self):

        localctx = GLSLPreParser.Version_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_version_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(GLSLPreParser.NUMBER_SIGN)
            self.state = 237
            self.match(GLSLPreParser.VERSION_DIRECTIVE)
            self.state = 238
            self.number()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==306:
                self.state = 239
                self.profile()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





