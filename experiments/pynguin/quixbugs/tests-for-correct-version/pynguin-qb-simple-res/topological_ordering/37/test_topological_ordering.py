# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    dict_0 = {}
    var_0 = module_0.topological_ordering(dict_0)


def test_case_1():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [node_0, node_0, node_0, node_0, node_0]
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    var_0 = module_0.topological_ordering(set_0)
    var_1 = module_2.object()
    node_0 = module_1.Node(successors=var_0, predecessors=set_0, incoming_nodes=var_1)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == {*()}
    assert (
        f"{type(node_0.incoming_nodes).__module__}.{type(node_0.incoming_nodes).__qualname__}"
        == "builtins.object"
    )
    assert node_0.outgoing_nodes == []
    list_0 = [node_0]
    var_2 = module_0.topological_ordering(list_0)
    node_1 = module_1.Node()
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert node_1.successors == []
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    node_1.successors()


def test_case_3():
    set_0 = set()
    node_0 = module_1.Node(successors=set_0, predecessors=set_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == {*()}
    assert node_0.predecessors == {*()}
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [node_0, node_0, node_0, node_0, node_0, node_0]
    node_1 = module_1.Node(predecessors=set_0, outgoing_nodes=list_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert node_1.successors == []
    assert node_1.predecessors == {*()}
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.outgoing_nodes) == 6
    dict_0 = {node_1: set_0}
    var_0 = module_0.topological_ordering(dict_0)