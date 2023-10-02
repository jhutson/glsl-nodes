import sys
from pathlib import Path

bl_info = {
    "name": "GLSL Nodes",
    "author": "Jimmy Hutson",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "Script tab in the Material editor",
    "description": "Creates nodes groups based on GLSL scripts",
    "category": "Node"
}

import bpy

module_path = str(Path(__file__).parent.resolve() / "modules")

if module_path not in sys.path:
    sys.path.append(str(module_path))

if "panels" not in locals():
    from . import glsl_ast
    from . import operators
    from . import panels
    from . import parser
else:
    import importlib
    glsl_ast = importlib.reload(glsl_ast)
    operators = importlib.reload(operators)
    panels = importlib.reload(panels)
    parser = importlib.reload(parser)


def register():

    operators.register()
    panels.register()


def unregister():
    panels.unregister()
    operators.unregister()


if __name__ == "__main__":
    register()