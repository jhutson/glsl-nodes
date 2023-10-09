from . import parser
from . import graph
from .visitor import GraphBuilder


def create_group_node_graph(file_path) -> graph.NodeGraph | graph.GraphError:
    """Parses the specified script file and attempts to map the script to the components of the Blender node group tree.
    It either returns the completed abstract graph or an error object.

    :param file_path: Path to the GLSL file
    :return: A graph. object that details how to construct the Blender node group,
             or a PlanError that describes the first issue that occurred during mapping.
    """
    try:
        script_root = parser.load(file_path)
        v = GraphBuilder()
        script_root.accept(v)

        return v.node_graph
    except ValueError as e:
        return graph.GraphError(str(e))
    except parser.UnsupportedError as ue:
        return graph.GraphError(f'unsupported {ue.rule_type}: {ue.text}')
