# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Fxgh48j9M,h5:"
    module_0.reverse_linked_list(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.reverse_linked_list(tuple_0)
    int_0 = -152
    module_0.reverse_linked_list(int_0)


def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(predecessors=none_type_0, outgoing_nodes=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is None
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors is None
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes is None
    var_1 = module_0.reverse_linked_list(none_type_0)
    var_2 = module_0.reverse_linked_list(var_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "n$Z2s3dx<XXIv\x0cQPe"
    node_0 = module_1.Node(successor=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == "n$Z2s3dx<XXIv\x0cQPe"
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.reverse_linked_list(node_0)