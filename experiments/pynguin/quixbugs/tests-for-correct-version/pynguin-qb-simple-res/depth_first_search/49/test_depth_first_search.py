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
    float_0 = -419.392
    none_type_0 = None
    module_0.depth_first_search(float_0, none_type_0)


def test_case_2():
    complex_0 = 825.9 + 3266.0899j
    node_0 = module_1.Node(complex_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == (825.9 + 3266.0899j)
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.depth_first_search(node_0, complex_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    list_0 = [dict_0, bool_0]
    node_0 = module_1.Node(successors=list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == [{True: True}, True]
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.depth_first_search(node_0, list_0)