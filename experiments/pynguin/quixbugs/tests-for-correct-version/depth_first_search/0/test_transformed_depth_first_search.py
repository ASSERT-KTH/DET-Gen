# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
#    module_0.depth_first_search(bool_0, set_0)


def test_case_2():
    bool_0 = True
    none_type_0 = None
    node_0 = module_1.Node(successor=bool_0, outgoing_nodes=none_type_0)
    var_0 = module_0.depth_first_search(node_0, none_type_0)
    assert var_0 is False


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "+X^nf"
    node_0 = module_1.Node(successors=str_0)
    list_0 = [node_0, str_0, node_0]
#    module_0.depth_first_search(node_0, list_0)
