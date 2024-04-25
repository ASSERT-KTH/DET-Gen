# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import reverse_linked_list as module_1
import node as module_2


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    set_0 = {object_0, object_0}
    module_1.reverse_linked_list(set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_1.reverse_linked_list(none_type_0)
    var_0.successors()


def test_case_2():
    pass


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -3192.4339
    set_0 = {float_0, float_0}
    node_0 = module_2.Node(
        successor=set_0, predecessors=set_0, incoming_nodes=set_0, outgoing_nodes=set_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert (
        f"{type(node_0.successor).__module__}.{type(node_0.successor).__qualname__}"
        == "builtins.set"
    )
    assert len(node_0.successor) == 1
    assert node_0.successors == []
    assert (
        f"{type(node_0.predecessors).__module__}.{type(node_0.predecessors).__qualname__}"
        == "builtins.set"
    )
    assert len(node_0.predecessors) == 1
    assert (
        f"{type(node_0.incoming_nodes).__module__}.{type(node_0.incoming_nodes).__qualname__}"
        == "builtins.set"
    )
    assert len(node_0.incoming_nodes) == 1
    assert (
        f"{type(node_0.outgoing_nodes).__module__}.{type(node_0.outgoing_nodes).__qualname__}"
        == "builtins.set"
    )
    assert len(node_0.outgoing_nodes) == 1
    module_1.reverse_linked_list(node_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ""
    var_0 = module_2.Node()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    var_1 = module_1.reverse_linked_list(var_0)
    assert f"{type(var_1).__module__}.{type(var_1).__qualname__}" == "node.Node"
    assert var_1.value is None
    assert var_1.successor is None
    assert var_1.successors == []
    assert var_1.predecessors == []
    assert var_1.incoming_nodes == []
    assert var_1.outgoing_nodes == []
    var_2 = module_1.reverse_linked_list(str_0)
    object_0 = module_0.object()
    module_1.reverse_linked_list(object_0)