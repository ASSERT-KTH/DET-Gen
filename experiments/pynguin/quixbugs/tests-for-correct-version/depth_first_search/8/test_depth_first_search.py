# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    str_0 = '"'
    var_0 = module_0.depth_first_search(str_0, str_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    none_type_0 = None
    module_0.depth_first_search(bool_0, none_type_0)


def test_case_2():
    bool_0 = True
    node_0 = module_1.Node(bool_0)
    set_0 = {bool_0, bool_0, bool_0}
    var_0 = module_0.depth_first_search(node_0, set_0)
    assert var_0 is False


def test_case_3():
    float_0 = -1080.62
    tuple_0 = (float_0,)
    node_0 = module_1.Node(successors=tuple_0)
    var_0 = module_0.depth_first_search(node_0, float_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_4():
    node_0 = module_1.Node()
    list_0 = [node_0, node_0, node_0]
    none_type_0 = None
    node_1 = module_1.Node(successors=list_0, predecessors=none_type_0)
    var_0 = module_0.depth_first_search(node_1, list_0)
    assert var_0 is False
    node_1.successors()
