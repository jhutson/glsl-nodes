import bpy
from glsl_compiler import parser
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
            root = parser.load(file_path)
            try:
                group = self._create_node_group(context, file_path.stem, root)

                # SHADER_SPECIFIC: active_material and ShaderNodeGroup
                group_node = context.object.active_material.node_tree.nodes.new('ShaderNodeGroup')
                group_node.node_tree = bpy.data.node_groups[group.name]
            except ValueError as e:
                print(e)
                self.report({"ERROR"}, f'Could not create node group from script')
                return {'CANCELLED'}
            return {'FINISHED'}
        else:
            self.report({"ERROR"}, f'Path does not exist or is not a file: {file_path}')
            return {'CANCELLED'}


    def _create_node_group(self, context, group_name, glsl_node):
        bpy.context.scene.use_nodes = True

        # SHADER_SPECIFIC: ShaderNodeTree
        group = bpy.data.node_groups.new(group_name, 'ShaderNodeTree')

        group_input = group.nodes.new("NodeGroupInput")
        group_output = group.nodes.new("NodeGroupOutput")

        for input_variable in self._get_variables_by_qualifier(glsl_node, "in"):
            group.inputs.new(self._get_socket_type(input_variable), input_variable.identifier.name)

        for input_variable in self._get_variables_by_qualifier(glsl_node, "out"):
            group.outputs.new(self._get_socket_type(input_variable), input_variable.identifier.name)

        return group


    def _get_variables_by_qualifier(self, glsl_node, qualifier):
        for variable in glsl_node.variable_list.variables:
            if variable.type.qualifier and variable.type.qualifier.name == qualifier:
                yield variable

    def _get_socket_type(self, variable_node):
        type_name = variable_node.type.specifier.name
        match type_name:
            case 'float':
                return "NodeSocketFloat"
            case _:
                raise ValueError(f'Unsupported mapping from {type_name} to node socket type')


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
