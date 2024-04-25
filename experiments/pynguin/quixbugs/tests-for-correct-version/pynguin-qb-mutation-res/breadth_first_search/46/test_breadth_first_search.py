# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    float_0 = -698.8651172078462
    var_0 = module_0.breadth_first_search(float_0, float_0)
    assert var_0 is True


def test_case_1():
    str_0 = "]"
    var_0 = module_0.breadth_first_search(str_0, str_0)
    assert var_0 is True
    var_1 = module_0.breadth_first_search(var_0, var_0)
    assert var_1 is True
    list_0 = [var_0, var_0, var_0, str_0]
    node_0 = module_1.Node(successors=list_0)
    assert node_0.successors == [True, True, True, "]"]
    var_2 = module_0.breadth_first_search(node_0, var_1)
    assert var_2 is True


def test_case_2():
    bool_0 = False
    node_0 = module_1.Node(bool_0, outgoing_nodes=bool_0)
    var_0 = module_0.breadth_first_search(node_0, bool_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "'"
    var_0 = module_1.Node(successors=str_0, predecessors=str_0)
    float_0 = 104.1077
    list_0 = [var_0, var_0, float_0, str_0, var_0]
    node_0 = module_1.Node(successors=list_0)
    module_0.breadth_first_search(node_0, str_0)