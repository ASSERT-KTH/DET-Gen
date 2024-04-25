# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    float_0 = -620.36375
    var_0 = module_0.depth_first_search(float_0, float_0)
    assert var_0 is True


def test_case_1():
    none_type_0 = None
    node_0 = module_1.Node(none_type_0, outgoing_nodes=none_type_0)
    var_0 = module_0.depth_first_search(node_0, none_type_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xac\xf8-"
    var_0 = module_0.depth_first_search(bytes_0, bytes_0)
    assert var_0 is True
    node_0 = module_1.Node(successors=bytes_0)
    module_0.depth_first_search(node_0, bytes_0)