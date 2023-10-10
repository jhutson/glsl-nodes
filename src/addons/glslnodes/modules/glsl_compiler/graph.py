from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class GraphError:
    message: str


@dataclass
class Socket:
    name: str
    socket_type: str


@dataclass(eq=False)
class Node:

    def input_count(self):
        pass


@dataclass(eq=False)
class GroupNode(Node):
    inputs: List[Socket] = field(default_factory=list)
    outputs: List[Socket] = field(default_factory=list)

    def input_count(self):
        return len(self.inputs)


@dataclass(eq=False)
class ValueNode(Node):
    value: float | int | bool

    def input_count(self):
        return 1


@dataclass(eq=False)
class MathNode(Node):
    operation: str
    _input_count: int

    def input_count(self):
        return self._input_count


@dataclass(frozen=True)
class SocketRef:
    socket_index: int
    node: Node


class NodeGraph:
    nodes: List[Node]
    links: Dict[SocketRef, List[SocketRef]]
    '''Map node A input (to node) to node B output (from node).
    
    Used to build node graph "backwards", that is, from the GroupOutput to the GroupInput.
    Given a node X, this can be used to find the nodes connected to its inputs.
    '''

    def __init__(self):
        self.nodes = []
        self.links = defaultdict(list)
        self.nodes.append(GroupNode())
        self.nodes.append(GroupNode())

    def get_group_input(self):
        return self.nodes[0]

    def get_group_output(self):
        return self.nodes[1]
