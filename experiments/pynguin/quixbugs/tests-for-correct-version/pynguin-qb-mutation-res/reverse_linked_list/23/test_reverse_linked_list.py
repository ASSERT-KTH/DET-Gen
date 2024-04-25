# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\nU\t7QJ@"
    bool_0 = False
    dict_0 = {str_0: bool_0}
    module_0.reverse_linked_list(dict_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    var_0 = module_0.reverse_linked_list(bool_0)
    node_0 = module_1.Node(predecessors=bool_0)
    var_1 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors is False
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == []
    var_1.successors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    node_0 = module_1.Node(predecessors=bool_0)
    tuple_0 = ()
    node_1 = module_1.Node(tuple_0, node_0, outgoing_nodes=node_0)
    var_0 = module_0.reverse_linked_list(bool_0)
    var_1 = module_0.reverse_linked_list(node_1)
    assert (
        f"{type(node_0.successor).__module__}.{type(node_0.successor).__qualname__}"
        == "node.Node"
    )
    assert node_1.successor is None
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert (
        f"{type(var_1.successor).__module__}.{type(var_1.successor).__qualname__}"
        == "node.Node"
    )
    assert var_1.successors == []
    assert var_1.predecessors is False
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == []
    var_2 = module_0.reverse_linked_list(node_1)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "node.Node"
    assert var_2.value == ()
    assert var_2.successor is None
    assert var_2.successors == []
    assert var_2.predecessors == []
    assert var_2.incoming_nodes == []
    assert (
        f"{type(var_2.outgoing_nodes).__module__}.{type(var_2.outgoing_nodes).__qualname__}"
        == "node.Node"
    )
    node_0.predecessors()