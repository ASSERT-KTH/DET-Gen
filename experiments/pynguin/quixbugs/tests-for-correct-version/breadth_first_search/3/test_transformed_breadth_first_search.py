# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    str_0 = "HWt"
    var_0 = module_0.breadth_first_search(str_0, str_0)
    assert var_0 is True


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3341
    var_0 = module_0.breadth_first_search(int_0, int_0)
    assert var_0 is True
#    module_0.breadth_first_search(int_0, var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"O\x88\xd4\x9b\xab\x1e\t\x0b"
    node_0 = module_1.Node(successors=bytes_0)
#    module_0.breadth_first_search(node_0, bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"O\x88\xd4\x9b\xab\x1e\t\x0b"
    node_0 = module_1.Node(bytes_0, predecessors=bytes_0, incoming_nodes=bytes_0)
    var_0 = module_0.breadth_first_search(node_0, bytes_0)
    assert var_0 is False
    var_1 = module_0.breadth_first_search(var_0, var_0)
    assert var_1 is True
    none_type_0 = None
    var_2 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_2 is True
#    module_0.breadth_first_search(none_type_0, var_1)
