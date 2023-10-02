import bpy
from bpy.props import StringProperty


class GLSLNODE_PT_Script(bpy.types.Panel):
    """Creates a Panel in the Shader Editor for GLSL Script Nodes"""
    bl_label = "GLSL Script Node"
    bl_idname = "GLSLNODE_PT_Script"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "GLSL Script"

    @classmethod
    def poll(self, context):
        return context.area.ui_type == "ShaderNodeTree"

    def draw(self, context):
        layout = self.layout

        # row = layout.row()
        # row.operator("glslnode.open_file_browser", text="Select File", icon="FILE_FOLDER")

        row = layout.row()
        # SHADER_SPECIFIC: active_material
        row.prop(context.object.active_material, "glslnode_script_path")

        script_path = context.object.active_material.glslnode_script_path

        row = layout.row()
        rowOp = row.operator("glslnode.create_node_group")
        rowOp.file_path = script_path
        row.enabled = not script_path == ""


def register():
    bpy.utils.register_class(GLSLNODE_PT_Script)

def unregister():
    bpy.utils.unregister_class(GLSLNODE_PT_Script)