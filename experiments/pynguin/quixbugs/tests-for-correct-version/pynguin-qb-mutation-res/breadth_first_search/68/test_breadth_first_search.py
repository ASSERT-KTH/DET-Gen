# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    str_0 = "[5#"
    var_0 = module_0.breadth_first_search(str_0, str_0)
    assert var_0 is True


def test_case_1():
    int_0 = -2275
    var_0 = module_1.Node()
    var_1 = module_0.breadth_first_search(var_0, int_0)
    assert var_1 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2275
    var_0 = module_0.breadth_first_search(int_0, int_0)
    assert var_0 is True
    module_0.breadth_first_search(var_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x80~\xff\x94Z\xddwQ"
    node_0 = module_1.Node(bytes_0, successors=bytes_0)
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x88"
    node_0 = module_1.Node(
        bytes_0, successors=bytes_0, predecessors=bytes_0, incoming_nodes=bytes_0
    )
    list_0 = [node_0, node_0, node_0]
    node_1 = module_1.Node(successor=bytes_0, successors=list_0, incoming_nodes=list_0)
    module_0.breadth_first_search(node_1, bytes_0)