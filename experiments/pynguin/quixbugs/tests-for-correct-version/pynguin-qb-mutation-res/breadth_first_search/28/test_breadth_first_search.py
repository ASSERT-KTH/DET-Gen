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
    bytes_0 = b"6\x1a"
    node_0 = module_1.Node(bytes_0, bytes_0, bytes_0, outgoing_nodes=bytes_0)
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    none_type_0 = None
    module_0.breadth_first_search(bool_0, none_type_0)


def test_case_3():
    bytes_0 = b"\x8b"
    node_0 = module_1.Node(predecessors=bytes_0)
    none_type_0 = None
    var_0 = module_0.breadth_first_search(node_0, none_type_0)
    assert var_0 is False
    object_0 = module_2.object()