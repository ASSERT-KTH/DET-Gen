# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True
    module_0.breadth_first_search(var_0, none_type_0)


def test_case_2():
    node_0 = module_1.Node()
    object_0 = module_2.object()
    var_0 = module_0.breadth_first_search(node_0, object_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    set_0 = {none_type_0, none_type_0, none_type_0}
    node_0 = module_1.Node(set_0, successors=set_0)
    module_0.breadth_first_search(node_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    set_0 = {none_type_0, none_type_0, none_type_0}
    node_0 = module_1.Node(set_0, successors=set_0)
    set_1 = {none_type_0, none_type_0, none_type_0, node_0}
    node_1 = module_1.Node(
        successor=none_type_0, successors=set_1, outgoing_nodes=none_type_0
    )
    module_0.breadth_first_search(node_1, set_0)