# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\tt.d9zP9=v ]VE8po;w\n"
    module_0.reverse_linked_list(str_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.reverse_linked_list(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(incoming_nodes=none_type_0)
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes is None
    assert var_0.outgoing_nodes == []
    var_0.successors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    var_0 = module_1.Node(predecessors=set_0)
    bytes_0 = b"\xa2\xd0\xdb\x03\x85\xec\xd8"
    node_0 = module_1.Node(
        successor=var_0,
        predecessors=var_0,
        incoming_nodes=bytes_0,
        outgoing_nodes=var_0,
    )
    var_1 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors == {*()}
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == []
    var_2 = module_0.reverse_linked_list(node_0)
    assert (
        f"{type(var_0.successor).__module__}.{type(var_0.successor).__qualname__}"
        == "node.Node"
    )
    assert node_0.successor is None
    assert (
        f"{type(var_1.successor).__module__}.{type(var_1.successor).__qualname__}"
        == "node.Node"
    )
    assert f"{type(var_2).__module__}.{type(var_2).__qualname__}" == "node.Node"
    assert var_2.value is None
    assert (
        f"{type(var_2.successor).__module__}.{type(var_2.successor).__qualname__}"
        == "node.Node"
    )
    assert var_2.successors == []
    assert var_2.predecessors == {*()}
    assert var_2.incoming_nodes == []
    assert var_2.outgoing_nodes == []
    var_3 = module_0.reverse_linked_list(var_2)
    assert (
        f"{type(node_0.successor).__module__}.{type(node_0.successor).__qualname__}"
        == "node.Node"
    )
    assert var_1.successor is None
    assert var_2.successor is None
    assert f"{type(var_3).__module__}.{type(var_3).__qualname__}" == "node.Node"
    assert var_3.value is None
    assert (
        f"{type(var_3.successor).__module__}.{type(var_3.successor).__qualname__}"
        == "node.Node"
    )
    assert var_3.successors == []
    assert (
        f"{type(var_3.predecessors).__module__}.{type(var_3.predecessors).__qualname__}"
        == "node.Node"
    )
    assert var_3.incoming_nodes == b"\xa2\xd0\xdb\x03\x85\xec\xd8"
    assert (
        f"{type(var_3.outgoing_nodes).__module__}.{type(var_3.outgoing_nodes).__qualname__}"
        == "node.Node"
    )
    var_4 = module_0.reverse_linked_list(var_0)
    assert f"{type(var_4).__module__}.{type(var_4).__qualname__}" == "node.Node"
    assert var_4.value is None
    assert var_4.successor is None
    assert var_4.successors == []
    assert var_4.predecessors == {*()}
    assert var_4.incoming_nodes == []
    assert var_4.outgoing_nodes == []
    var_5 = module_0.reverse_linked_list(var_4)
    assert f"{type(var_5).__module__}.{type(var_5).__qualname__}" == "node.Node"
    assert var_5.value is None
    assert var_5.successor is None
    assert var_5.successors == []
    assert var_5.predecessors == {*()}
    assert var_5.incoming_nodes == []
    assert var_5.outgoing_nodes == []
    var_2.successor()