from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Socket:
    name: str
    socket_type: str


@dataclass(eq=False)
class Node:
    inputs: List[Socket]
    outputs: List[Socket]


@dataclass(eq=False, init=False)
class ValueNode(Node):
    value: float | int | bool

    def __init__(self, value: float | int | bool, socket: Socket):
        super().__init__([], [socket])
        self.value = value


@dataclass(eq=False, init=False)
class MathNode(Node):
    operator: str

    def __init__(self, operator: str, inputs: List[Socket], output: Socket):
        super().__init__(inputs, [output])
        self.operator = operator


@dataclass(frozen=True)
class SocketRef:
    socket_index: int
    node: Node

    def get_output_type(self):
        """Return socket type of node output socket at index referenced by this object.

        This should only be used when this object actually represents an output socket.
        """
        return self.node.outputs[self.socket_index].socket_type

class NodeGraph:
    nodes: List[Node]
    links: Dict[SocketRef, List[SocketRef]]
    '''Map node A input (to node) to node B output (from node).
    
    Used to build node graph "backwards", that is, from the GroupOutput to the GroupInput.
    Given a node X, this can be used to find the nodes connected to its inputs.
    '''

    def __init__(self, group_input: Node, group_output: Node):
        self.nodes = []
        self.links = defaultdict(list)
        self.nodes.append(group_output)
        self.nodes.append(group_input)

    def get_group_input(self):
        return self.nodes[1]

    def get_group_output(self):
        return self.nodes[0]
