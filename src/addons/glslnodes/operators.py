import bpy
from glsl_compiler import graph, builder
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
            result = builder.create_group_node_graph(file_path)
            match result:
                case graph.GraphError():
                    self.report({"ERROR"}, result.message)
                    return {'CANCELLED'}
                case graph.NodeGraph():
                    group = self._create_node_group(context, file_path.stem, result)
                    # SHADER_SPECIFIC: active_material and ShaderNodeGroup
                    group_node = context.object.active_material.node_tree.nodes.new('ShaderNodeGroup')
                    group_node.node_tree = bpy.data.node_groups[group.name]
                    return {'FINISHED'}
        else:
            self.report({"ERROR"}, f'Path does not exist or is not a file: {file_path}')
            return {'CANCELLED'}

    def _create_node_group(self, context, group_name, node_graph):
        bpy.context.scene.use_nodes = True

        # SHADER_SPECIFIC: ShaderNodeTree
        group = bpy.data.node_groups.new(group_name, 'ShaderNodeTree')

        index_by_node = {}
        real_nodes = []

        for index, node in enumerate(node_graph.nodes):
            index_by_node[node] = index
            match index:
                case 0:
                    group_input = group.nodes.new("NodeGroupInput")
                    for output_socket in node.outputs:
                        group.inputs.new(output_socket.socket_type, output_socket.name)
                    real_nodes.append(group_input)
                case 1:
                    group_output = group.nodes.new("NodeGroupOutput")
                    for output_socket in node.inputs:
                        group.outputs.new(output_socket.socket_type, output_socket.name)
                    real_nodes.append(group_output)
                case _:
                    match node:
                        case graph.ValueNode():
                            # SHADER_SPECIFIC: ShaderNodeValue
                            value_node = group.nodes.new("ShaderNodeValue")
                            value_node.outputs[0].default_value = node.value
                            real_nodes.append(value_node)
                        case graph.MathNode():
                            # SHADER_SPECIFIC: ShaderNodeMath
                            math_node = group.nodes.new("ShaderNodeMath")
                            math_node.operation = node.operation
                            real_nodes.append(math_node)

        for input_ref in node_graph.links:
            in_index = index_by_node[input_ref.node]
            in_node = real_nodes[in_index]

            for output_ref in node_graph.links[input_ref]:
                out_index = index_by_node[output_ref.node]
                out_node = real_nodes[out_index]

                group.links.new(in_node.inputs[input_ref.socket_index], out_node.outputs[output_ref.socket_index])

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
