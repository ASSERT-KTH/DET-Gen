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
    bytes_0 = b"9\x90\x1d\xf1\xf1\x07\xebL\x94\xc8\xad"
    node_0 = module_1.Node(successors=bytes_0)
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1044
    var_0 = module_0.breadth_first_search(int_0, int_0)
    assert var_0 is True
    module_0.breadth_first_search(var_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    node_0 = module_1.Node(incoming_nodes=none_type_0)
    var_0 = module_0.breadth_first_search(node_0, none_type_0)
    assert var_0 is False
    var_0.predecessors()