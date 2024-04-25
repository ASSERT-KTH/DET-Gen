# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True


def test_case_1():
    none_type_0 = None
    node_0 = module_1.Node(successor=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.depth_first_search(node_0, none_type_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True
    none_type_1 = None
    str_0 = "cA\x0bU^yY#:|eTpJlw"
    node_0 = module_1.Node(
        successors=str_0,
        predecessors=none_type_0,
        incoming_nodes=none_type_1,
        outgoing_nodes=var_0,
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "cA\x0bU^yY#:|eTpJlw"
    assert node_0.predecessors is None
    assert node_0.incoming_nodes is None
    assert node_0.outgoing_nodes is True
    module_0.depth_first_search(node_0, var_0)