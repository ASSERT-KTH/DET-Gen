# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "SUlE&Cu)ld2)\x0b}5"
    node_0 = module_1.Node(str_0, successors=str_0, incoming_nodes=str_0)
    module_0.breadth_first_search(node_0, str_0)


def test_case_2():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0}
    node_0 = module_1.Node(successor=set_0, predecessors=set_0, incoming_nodes=bool_0)
    none_type_0 = None
    var_0 = module_0.breadth_first_search(node_0, none_type_0)
    assert var_0 is False