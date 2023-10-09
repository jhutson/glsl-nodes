import typing
from collections import deque
from dataclasses import dataclass

import pytest
from pathlib import Path

from glsl_compiler import parser, visitor, graph


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


@pytest.fixture(scope="module")
def get_files_for_test_case(request, script_folder, baselines_folder, actual_folder):
    def _get(script_file_name):
        script_file = script_folder / script_file_name
        output_file = script_file.stem + ".txt"
        baseline_file = baselines_folder / output_file
        actual_file = actual_folder / output_file
        return FileLocations(script_file, baseline_file, actual_file)

    yield _get

    if request.session.testsfailed:
        print(f"To update baselines, run:\nmv {actual_folder / '*'} {baselines_folder.absolute()}")


def get_script_files():
    return [c.name for c in _script_folder().iterdir()]


@pytest.mark.parametrize('script_file', get_script_files())
def test_parser_with_script(script_file, get_files_for_test_case, capfd):
    files = get_files_for_test_case(script_file)
    root = parser.load(str(files.script_file))
    assert (root is not None)
    root.accept(visitor.Printer())

    baseline = files.baseline_file
    actual = files.actual_file

    logged = capfd.readouterr()
    actual.write_text(logged.err + logged.out)

    if not baseline.exists():
        assert False, f"No baseline file {baseline}, actual written to {actual}"

    assert actual.read_text() == baseline.read_text(), \
        f"actual {actual} differs from baseline {baseline}"


def test_graph_build(script_folder):
    root = parser.load(str(script_folder / "bin_ops_only.frag"))
    assert (root is not None)

    v = visitor.GraphBuilder()
    root.accept(v)

    g = v.node_graph

    index_by_node = {n: i for i, n in enumerate(g.nodes)}
    # Simulate creating actual nodes
    node_labels = [f"{type(n).__name__}{i}" for i, n in enumerate(g.nodes)]

    queue: typing.Deque[graph.Node] = deque()
    queue.append(g.get_group_output())
    visited: typing.Set[int] = set()

    print('Graph Links:')
    while len(queue) > 0:
        node = queue.pop()
        node_index = index_by_node[node]
        to_label = node_labels[node_index]
        visited.add(node_index)

        for input_ref in (graph.SocketRef(i, node) for i in range(0, node.input_count())):
            input_index = input_ref.socket_index
            for output_ref in g.links.get(input_ref, []):
                other_index = index_by_node[output_ref.node]
                from_label = node_labels[other_index]
                print(f'link {from_label}.outputs[{output_ref.socket_index}] to {to_label}.inputs[{input_index}]')

                if other_index not in visited:
                    queue.append(output_ref.node)
