# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.reverse_linked_list(bool_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.reverse_linked_list(set_0)
    var_1 = module_0.reverse_linked_list(set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(
        successors=none_type_0,
        predecessors=none_type_0,
        incoming_nodes=none_type_0,
        outgoing_nodes=none_type_0,
    )
    none_type_1 = None
    var_0 = module_0.reverse_linked_list(none_type_1)
    var_1 = module_0.reverse_linked_list(none_type_1)
    var_2 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "node.Node"
    assert var_2.value is None
    assert var_2.successor is None
    assert var_2.successors is None
    assert var_2.predecessors is None
    assert var_2.incoming_nodes is None
    assert var_2.outgoing_nodes is None
    bool_0 = True
    var_3 = module_0.reverse_linked_list(var_0)
    module_0.reverse_linked_list(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    node_0 = module_1.Node()
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    bool_0 = False
    var_1 = module_1.Node(bool_0, var_0, predecessors=var_0, incoming_nodes=var_0)
    assert (
        f"{type(var_1.successor).__module__}.{type(var_1.successor).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(var_1.predecessors).__module__}.{type(var_1.predecessors).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(var_1.incoming_nodes).__module__}.{type(var_1.incoming_nodes).__qualname__}"
        == "node.Node"
    )
    none_type_0 = None
    var_2 = module_0.reverse_linked_list(none_type_0)
    var_3 = module_0.reverse_linked_list(none_type_0)
    var_4 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_4).__module__}.{type(var_4).__qualname__}" == "node.Node"
    assert var_4.value is None
    assert var_4.successor is None
    assert var_4.successors == []
    assert var_4.predecessors == []
    assert var_4.incoming_nodes == []
    assert var_4.outgoing_nodes == []
    set_0 = set()
    var_5 = module_0.reverse_linked_list(set_0)
    var_6 = module_0.reverse_linked_list(var_1)
    assert (
        f"{type(node_0.successor).__module__}.{type(node_0.successor).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(var_0.successor).__module__}.{type(var_0.successor).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(var_4.successor).__module__}.{type(var_4.successor).__qualname__}"
        == "node.Node"
    )
    assert f"{type(var_6).__module__}.{type(var_6).__qualname__}" == "node.Node"
    assert var_6.value is None
    assert (
        f"{type(var_6.successor).__module__}.{type(var_6.successor).__qualname__}"
        == "node.Node"
    )
    assert var_6.successors == []
    assert var_6.predecessors == []
    assert var_6.incoming_nodes == []
    assert var_6.outgoing_nodes == []
    var_7 = module_0.reverse_linked_list(node_0)
    assert var_0.successor is None
    assert (
        f"{type(var_1.successor).__module__}.{type(var_1.successor).__qualname__}"
        == "node.Node"
    )
    assert var_4.successor is None
    assert var_6.successor is None
    assert f"{type(var_7).__module__}.{type(var_7).__qualname__}" == "node.Node"
    assert var_7.value is False
    assert (
        f"{type(var_7.successor).__module__}.{type(var_7.successor).__qualname__}"
        == "node.Node"
    )
    assert var_7.successors == []
    assert (
        f"{type(var_7.predecessors).__module__}.{type(var_7.predecessors).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(var_7.incoming_nodes).__module__}.{type(var_7.incoming_nodes).__qualname__}"
        == "node.Node"
    )
    assert var_7.outgoing_nodes == []
    var_3.successor()