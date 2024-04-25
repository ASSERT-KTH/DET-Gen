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
    float_0 = -1353.938
    node_0 = module_1.Node(successor=float_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == pytest.approx(-1353.938, abs=0.01, rel=0.01)
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    set_0 = {float_0}
    var_0 = module_0.depth_first_search(node_0, set_0)
    assert var_0 is False


def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(incoming_nodes=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes is None
    assert node_0.outgoing_nodes == []
    tuple_0 = (node_0, node_0)
    node_1 = module_1.Node(tuple_0, successors=tuple_0, predecessors=tuple_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.value) == 2
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.successors) == 2
    assert (
        f"{type(node_1.predecessors).__module__}.{type(node_1.predecessors).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.predecessors) == 2
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    var_0 = module_0.depth_first_search(node_1, none_type_0)
    assert var_0 is False
    float_0 = -1350.9029500574093
    node_2 = module_0.depth_first_search(float_0, float_0)
    assert node_2 is True