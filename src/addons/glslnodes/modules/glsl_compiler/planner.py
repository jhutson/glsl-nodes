from dataclasses import dataclass, field

from . import parser
from . import glsl_ast as ast


def _get_socket_type(variable_node):
    type_name = variable_node.type.specifier.name
    match type_name:
        case 'float':
            return "NodeSocketFloat"
        case _:
            raise ValueError(f"Unsupported mapping from '{type_name}' to node socket type for variable '{variable_node.identifier.name}'")


def _get_group_sockets(script_node: ast.Script, qualifier: str):
    variables = _get_variables_by_qualifier(script_node, qualifier)
    return [GroupNodeSocket(v.identifier.name, _get_socket_type(v)) for v in variables]


def _get_variables_by_qualifier(script_node: ast.Script, qualifier: str):
    for variable in script_node.variable_list.variables:
        if variable.type.qualifier and variable.type.qualifier.name == qualifier:
            yield variable


@dataclass
class PlanError:
    message: str

@dataclass
class GroupNodeSocket:
    name: str
    socket_type: str


@dataclass(eq=False)
class GroupNodePlan:
    inputs: list[GroupNodeSocket]
    outputs: list[GroupNodeSocket]


def create_group_node_plan(file_path):
    """Parses the specified script file and attempts to map the script to the components of the Blender node group tree.
    It either returns the completed plan or an error object.

    :param file_path: Path to the GLSL file
    :return: A GroupNodePlan object that details how to construct the Blender node group,
             or a PlanError that describes the first issue that occurred during mapping.
    """
    try:
        script_root = parser.load(file_path)
        inputs = _get_group_sockets(script_root, "in")
        if not inputs:
            return PlanError("Need at least one group input")

        outputs = _get_group_sockets(script_root, "out")
        if not outputs:
            return PlanError("Need at least one group output")

        plan = GroupNodePlan(inputs, outputs)
        return plan
    except ValueError as e:
        return PlanError(str(e))
    except parser.UnsupportedError as ue:
        return PlanError(f'unsupported {ue.rule_type}: {ue.text}')

