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
    float_0 = -1081.05
    node_0 = module_1.Node(float_0, float_0, incoming_nodes=float_0)
    str_0 = '+=!}+|5tGc"aD%a'
    list_0 = [node_0, node_0, str_0]
    node_1 = module_1.Node(
        successors=list_0, incoming_nodes=list_0, outgoing_nodes=list_0
    )
    none_type_0 = None
#    module_0.depth_first_search(node_1, none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc9\xf1\n?%\x18\xeb\xb1\xc1\x0fn"
    none_type_0 = None
#    module_0.depth_first_search(bytes_0, none_type_0)
