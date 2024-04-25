# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import reverse_linked_list as module_1
import node as module_2


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.reverse_linked_list(object_0)


def test_case_1():
    set_0 = set()
    var_0 = module_1.reverse_linked_list(set_0)


def test_case_2():
    node_0 = module_2.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_1.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    node_0 = module_2.Node(successor=bool_0, outgoing_nodes=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is True
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is True
    module_1.reverse_linked_list(node_0)