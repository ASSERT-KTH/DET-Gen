# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "|'__>.U\naWav~^ty{w@"
#    module_0.reverse_linked_list(str_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    bytes_0 = b"\xc6\t,*\xea\xe4q`\xf3\x04K\xdb"
    node_0 = module_1.Node(bytes_0, successors=none_type_0)
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value == b"\xc6\t,*\xea\xe4q`\xf3\x04K\xdb"
    assert var_0.successor is None
    assert var_0.successors is None
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
#    var_0.successor()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    var_0 = module_0.reverse_linked_list(tuple_0)
    node_0 = module_1.Node(predecessors=tuple_0)
    var_1 = module_1.Node(successor=node_0, predecessors=var_0)
    var_2 = module_0.reverse_linked_list(var_0)
    var_3 = module_0.reverse_linked_list(var_1)
    assert (
        f"{type(node_0.successor).__module__}.{type(node_0.successor).__qualname__}"
        == "node.Node"
    )
    assert var_1.successor is None
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "node.Node"
    assert var_3.value is None
    assert (
        f"{type(var_3.successor).__module__}.{type(var_3.successor).__qualname__}"
        == "node.Node"
    )
    assert var_3.successors == []
    assert var_3.predecessors == ()
    assert var_3.incoming_nodes == []
    assert var_3.outgoing_nodes == []
    var_4 = module_0.reverse_linked_list(var_0)
#    var_3.successor()
