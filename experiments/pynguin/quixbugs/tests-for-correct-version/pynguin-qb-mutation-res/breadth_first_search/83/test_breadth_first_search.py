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
    str_0 = "#&O*3%D+)[1cun/{`\t"
    node_0 = module_1.Node(successor=str_0, successors=str_0)
    module_0.breadth_first_search(node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    var_0 = module_0.breadth_first_search(bool_0, bool_0)
    assert var_0 is True
    module_0.breadth_first_search(var_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"R"
    var_0 = module_0.breadth_first_search(bytes_0, bytes_0)
    assert var_0 is True
    var_1 = module_0.breadth_first_search(bytes_0, bytes_0)
    assert var_1 is True
    int_0 = -3725
    node_0 = module_1.Node(bytes_0, bytes_0, predecessors=bytes_0, outgoing_nodes=int_0)
    int_1 = -545
    var_2 = module_0.breadth_first_search(node_0, int_1)
    var_2.successors()