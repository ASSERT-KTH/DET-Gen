# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "lMDO&n\rMhNrg|^5\n"
    module_0.shortest_paths(str_0, str_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.shortest_paths(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    bytes_0 = b"\x0e\x02"
    var_0 = module_0.shortest_paths(bytes_0, tuple_0)
    module_0.shortest_paths(tuple_0, var_0)


def test_case_3():
    tuple_0 = ()
    node_0 = module_1.Node(tuple_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == ()
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    bytes_0 = b"\x0e\x0e"
    var_0 = module_0.shortest_paths(bytes_0, tuple_0)
    var_1 = module_0.shortest_paths(node_0, var_0)
    bool_0 = False
    node_1 = module_1.Node(successor=var_0, outgoing_nodes=bool_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor == {b"\x0e\x0e": 0}
    assert node_1.successors == []
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes is False