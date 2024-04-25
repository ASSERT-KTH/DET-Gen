# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.breadth_first_search(bool_0, bool_0)
    assert var_0 is True


def test_case_1():
    bool_0 = True
    node_0 = module_1.Node(bool_0, predecessors=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is True
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors is True
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_0, bool_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x92\x94"
    none_type_0 = None
    module_0.breadth_first_search(bytes_0, none_type_0)


def test_case_3():
    str_0 = "&"
    node_0 = module_1.Node(successors=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "&"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_0, str_0)
    assert var_0 is True