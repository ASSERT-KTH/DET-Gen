# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb8\xa1\xe3{\xcfUR&\xd1\xa1"
#    module_0.reverse_linked_list(bytes_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.reverse_linked_list(tuple_0)
    var_1 = module_0.reverse_linked_list(var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    node_0 = module_1.Node(successor=bool_0, successors=bool_0, predecessors=bool_0)
    var_0 = module_0.reverse_linked_list(node_0)
    assert node_0.successor is None
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors is False
    assert var_0.predecessors is False
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    var_1 = module_0.reverse_linked_list(bool_0)
#    var_1.successors()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    node_0 = module_1.Node(successor=bool_0, successors=bool_0, predecessors=bool_0)
#    module_0.reverse_linked_list(node_0)
