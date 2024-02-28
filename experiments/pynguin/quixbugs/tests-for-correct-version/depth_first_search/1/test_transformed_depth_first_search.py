# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    int_0 = 1273
    var_0 = module_0.depth_first_search(int_0, int_0)
    assert var_0 is True


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.depth_first_search(none_type_0, none_type_0)
    assert var_0 is True
    bytes_0 = b"6\xc9c\xa5"
#    module_0.depth_first_search(none_type_0, bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    node_0 = module_1.Node(predecessors=bool_0, outgoing_nodes=bool_0)
    var_0 = module_0.depth_first_search(node_0, bool_0)
    assert var_0 is False
#    module_0.depth_first_search(var_0, node_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\\\x0e\xfc"
    set_0 = set()
    tuple_0 = (bytes_0, bytes_0, set_0)
    node_0 = module_1.Node(successors=tuple_0)
#    module_0.depth_first_search(node_0, set_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    list_0 = []
    node_0 = module_1.Node(outgoing_nodes=list_0)
    list_1 = [node_0, node_0, node_0, node_0]
    node_1 = module_1.Node(successors=list_1)
    none_type_0 = None
    var_0 = module_0.depth_first_search(node_1, none_type_0)
    assert var_0 is False
#    module_0.depth_first_search(var_0, node_1)
