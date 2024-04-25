# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.depth_first_search(bool_0, bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    var_0 = module_1.Node(successor=bool_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is True
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    bool_1 = True
    var_1 = module_0.depth_first_search(var_0, set_0)
    assert var_1 is False
    tuple_0 = (bool_1,)
    module_0.depth_first_search(tuple_0, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 2858.9003
    tuple_0 = (float_0,)
    module_0.depth_first_search(tuple_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -482
    list_0 = []
    var_0 = module_0.depth_first_search(int_0, int_0)
    assert var_0 is True
    int_1 = 4309
    dict_0 = {int_0: int_0, var_0: int_0, var_0: int_1, int_1: int_0}
    tuple_0 = (int_0, int_0, list_0, dict_0)
    node_0 = module_1.Node(successors=tuple_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == (-482, -482, [], {-482: -482, True: 4309, 4309: -482})
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.depth_first_search(node_0, tuple_0)