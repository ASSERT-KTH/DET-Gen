# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    dict_0 = {}
    var_0 = module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\rz\xc8N?\x02&\x10\xb3'I\xc2\xc9=\xbb\x0b"
    module_0.topological_ordering(bytes_0)


def test_case_2():
    node_0 = module_1.Node()
    set_0 = {node_0, node_0, node_0, node_0}
    var_0 = module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    node_0 = module_1.Node(
        tuple_0, tuple_0, predecessors=bool_0, outgoing_nodes=tuple_0
    )
    set_0 = {node_0}
    module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xf2:\xca\x1e\xb8_\x95\xd6\x0f\xc9\x91\xd9:\xf8\x1c\x93"
    node_0 = module_1.Node(bytes_0, incoming_nodes=bytes_0)
    bytes_1 = b"2\xd0\xa4"
    tuple_0 = (node_0, node_0, bytes_1)
    module_0.topological_ordering(tuple_0)