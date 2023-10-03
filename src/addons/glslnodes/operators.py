import bpy
from glsl_compiler import planner
from bpy.types import Operator
from bpy.props import StringProperty
from pathlib import Path


class GLSLNODE_OT_CreateNodeGroup(Operator):
    """Create Node Group from Script File"""
    bl_idname = "glslnode.create_node_group"
    bl_label = "Create Node Group"

    file_path: StringProperty(subtype="FILE_PATH")

    @classmethod
    def poll(cls, context):
        # space = context.space_data
        # return space.type == 'NODE_EDITOR'
        return context.area.ui_type == "ShaderNodeTree"

    def execute(self, context):
        file_path = Path(bpy.path.abspath(self.file_path))
        file_path = file_path.resolve()

        if file_path.exists() and file_path.is_file():
            result = planner.create_group_node_plan(file_path)
            match result:
                case planner.PlanError():
                    self.report({"ERROR"}, result.message)
                    return {'CANCELLED'}
                case planner.GroupNodePlan():
                    group = self._create_node_group(context, file_path.stem, result)
                    # SHADER_SPECIFIC: active_material and ShaderNodeGroup
                    group_node = context.object.active_material.node_tree.nodes.new('ShaderNodeGroup')
                    group_node.node_tree = bpy.data.node_groups[group.name]
                    return {'FINISHED'}
        else:
            self.report({"ERROR"}, f'Path does not exist or is not a file: {file_path}')
            return {'CANCELLED'}

    def _create_node_group(self, context, group_name, group_plan):
        bpy.context.scene.use_nodes = True

        # SHADER_SPECIFIC: ShaderNodeTree
        group = bpy.data.node_groups.new(group_name, 'ShaderNodeTree')

        group_input = group.nodes.new("NodeGroupInput")
        group_output = group.nodes.new("NodeGroupOutput")

        for input_socket in group_plan.inputs:
            group.inputs.new(input_socket.socket_type, input_socket.name)

        for output_socket in group_plan.outputs:
            group.outputs.new(output_socket.socket_type, output_socket.name)

        return group


def register():
    bpy.utils.register_class(GLSLNODE_OT_CreateNodeGroup)
    # bpy.utils.register_class(GLSLNODE_OT_OpenFileBrowser)

    # SHADER_SPECIFIC: Material
    bpy.types.Material.glslnode_script_path = StringProperty(
        name="Script File",
        default="",
        subtype="FILE_PATH",
        options={"HIDDEN", "SKIP_SAVE"})


def unregister():
    del bpy.types.Material.glslnode_script_path

    bpy.utils.unregister_class(GLSLNODE_OT_CreateNodeGroup)
    # bpy.utils.unregister_class(GLSLNODE_OT_OpenFileBrowser)
