# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.breadth_first_search(bool_0, bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "sq"
    node_0 = module_1.Node(successors=str_0, incoming_nodes=str_0)
    module_0.breadth_first_search(node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -3423
    tuple_0 = (int_0, int_0, int_0, int_0)
    node_0 = module_1.Node(predecessors=tuple_0)
    var_0 = module_0.breadth_first_search(node_0, tuple_0)
    assert var_0 is False
    node_0.predecessors()