# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    str_0 = "\x0ck"
    var_0 = module_0.breadth_first_search(str_0, str_0)
    assert var_0 is True


def test_case_1():
    float_0 = 3155.8538
    node_0 = module_1.Node(outgoing_nodes=float_0)
    var_0 = module_0.breadth_first_search(node_0, float_0)
    assert var_0 is False


def test_case_2():
    str_0 = "\r"
    node_0 = module_1.Node(successor=str_0, successors=str_0, outgoing_nodes=str_0)
    var_0 = module_0.breadth_first_search(node_0, str_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\r"
    node_0 = module_1.Node(successor=str_0, successors=str_0, outgoing_nodes=str_0)
    list_0 = [node_0, str_0, str_0, node_0]
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True
    node_1 = module_1.Node(successors=list_0, predecessors=none_type_0)
    module_0.breadth_first_search(node_1, none_type_0)
