import typing
from collections import deque
from dataclasses import dataclass

import pytest
from pathlib import Path

from glsl_compiler import builder, graph, parser
from tests.visitor import Printer


def _script_folder():
    base_path = Path(".") / "tests"
    return base_path / "scripts"


@pytest.fixture(scope="module")
def script_folder():
    return _script_folder()


@pytest.fixture(scope="module")
def baselines_folder():
    base_path = Path(".") / "tests"
    return base_path / "baselines"


@pytest.fixture(scope="module")
def actual_folder(tmp_path_factory):
    return tmp_path_factory.mktemp("actual")


@dataclass
class FileLocations:
    script_file: Path
    baseline_file: Path
    actual_file: Path


@pytest.fixture()
def get_files_for_test_case(request, script_folder, baselines_folder, actual_folder):
    test_name = request.node.originalname
    test_baseline_folder = baselines_folder / test_name
    test_actual_folder = actual_folder / test_name
    test_actual_folder.mkdir(exist_ok=True)

    def _get(script_file_name):
        script_file = script_folder / script_file_name
        output_file = script_file.stem + ".txt"
        baseline_file = test_baseline_folder / output_file
        actual_file = test_actual_folder / output_file
        return FileLocations(script_file, baseline_file, actual_file)

    failed_test_count = request.session.testsfailed
    yield _get

    if request.session.testsfailed > failed_test_count:
        print(f"To update baselines, run:\nmv {test_actual_folder / '*'} {test_baseline_folder.absolute()}")


def get_script_files():
    return [c.name for c in _script_folder().iterdir()]


def _compare_actual_to_baseline(files: FileLocations, capfd):
    baseline = files.baseline_file
    actual = files.actual_file

    logged = capfd.readouterr()
    actual.write_text(logged.err + logged.out)

    if not baseline.exists():
        assert False, f"No baseline file {baseline}, actual written to {actual}"

    assert actual.read_text() == baseline.read_text(), \
        f"actual {actual} differs from baseline {baseline}"


@pytest.mark.parametrize('script_file', get_script_files())
def test_parser_with_script(script_file, get_files_for_test_case, capfd):
    files = get_files_for_test_case(script_file)
    root = parser.load(files.script_file)
    assert (root is not None)
    root.accept(Printer())

    _compare_actual_to_baseline(files, capfd)


@pytest.mark.parametrize('script_file', get_script_files())
def test_graph_build(script_file, script_folder, get_files_for_test_case, capfd):
    def socket_label(socket_ref: graph.SocketRef, is_input: bool):
        match socket_ref:
            case graph.SocketRef(i, graph.GroupNode() as group_node):
                if is_input:
                    return str(group_node.inputs[i])
                else:
                    return str(group_node.outputs[i])
            case _:
                return socket_ref.socket_index

    files = get_files_for_test_case(script_file)
    g = builder.create_group_node_graph(files.script_file)

    match g:
        case graph.GraphError(message):
            print(f"GraphError: {message}")
        case _:
            index_by_node = {n: i for i, n in enumerate(g.nodes)}
            # Simulate creating actual nodes
            node_labels = [f"{str(n)}-{i}" for i, n in enumerate(g.nodes)]

            print('All Nodes:')
            for label in node_labels:
                print(label)

            print('\nAll Links:')
            for input_ref in g.links:
                in_index = index_by_node[input_ref.node]
                to_label = node_labels[in_index]
                to_socket_label = f"{to_label}.inputs[{socket_label(input_ref, True)}]"

                for output_ref in g.links[input_ref]:
                    out_index = index_by_node[output_ref.node]
                    from_label = node_labels[out_index]
                    print(f'link {from_label}.outputs[{socket_label(output_ref, False)}] to {to_socket_label}')

            queue: typing.Deque[graph.Node] = deque()
            queue.append(g.get_group_output())
            visited: typing.Set[int] = set()

            print('\nGraph Links Reachable from Group Output:')
            while len(queue) > 0:
                node = queue.pop()
                node_index = index_by_node[node]
                to_label = node_labels[node_index]
                visited.add(node_index)

                for input_ref in (graph.SocketRef(i, node) for i in range(0, node.input_count())):
                    to_socket_label = f"{to_label}.inputs[{socket_label(input_ref, True)}]"
                    for output_ref in g.links.get(input_ref, []):
                        other_index = index_by_node[output_ref.node]
                        from_label = node_labels[other_index]
                        print(f'link {from_label}.outputs[{socket_label(output_ref, False)}] to {to_socket_label}')

                        if other_index not in visited:
                            queue.append(output_ref.node)
            print("-END-")

    _compare_actual_to_baseline(files, capfd)
