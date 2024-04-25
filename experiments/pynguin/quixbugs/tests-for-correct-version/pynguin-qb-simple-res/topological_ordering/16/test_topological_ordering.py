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
    int_0 = 2579
    list_0 = [int_0, int_0, int_0, int_0]
    module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.topological_ordering(bool_0)


def test_case_3():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    tuple_0 = (node_0,)
    var_0 = module_0.topological_ordering(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x00\xaf\xc0G\xa9\xe0\x15\xac&\x03\x0f\x8b\xddl\xa8f\xf4\xbf\xe2"
    bytes_1 = b"\xa0\xb2\xcd\xbc\xd5\xb4\xc0\xc9\xe1"
    none_type_0 = None
    node_0 = module_1.Node(
        successors=none_type_0, predecessors=bytes_0, incoming_nodes=bytes_1
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors is None
    assert (
        node_0.predecessors
        == b"\x00\xaf\xc0G\xa9\xe0\x15\xac&\x03\x0f\x8b\xddl\xa8f\xf4\xbf\xe2"
    )
    assert node_0.incoming_nodes == b"\xa0\xb2\xcd\xbc\xd5\xb4\xc0\xc9\xe1"
    assert node_0.outgoing_nodes == []
    list_0 = [node_0]
    var_0 = module_0.topological_ordering(list_0)
    tuple_0 = ()
    var_1 = module_0.topological_ordering(tuple_0)
    list_1 = [tuple_0, tuple_0]
    list_2 = [tuple_0, list_1, list_1, tuple_0]
    module_0.topological_ordering(list_2)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x00\xaf\xc0\xa9\xe0\x15\xac&\x03\x0f\x8b\xddl\xa8f\xf4\xbf\xe2"
    none_type_0 = None
    node_0 = module_1.Node(
        successors=none_type_0, predecessors=none_type_0, outgoing_nodes=bytes_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors is None
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert (
        node_0.outgoing_nodes
        == b"\x00\xaf\xc0\xa9\xe0\x15\xac&\x03\x0f\x8b\xddl\xa8f\xf4\xbf\xe2"
    )
    list_0 = [node_0]
    module_0.topological_ordering(list_0)