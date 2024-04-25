# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    var_0 = module_0.topological_ordering(list_0)
    bool_0 = False
    module_0.topological_ordering(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"_=&\x13\x9e\x97{p]\x90\xdd\x8e\xe2\xd2\xe1\xae\x10"
    module_0.topological_ordering(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.topological_ordering(none_type_0)


def test_case_3():
    tuple_0 = ()
    node_0 = module_1.Node(successors=tuple_0, predecessors=tuple_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == ()
    assert node_0.predecessors == ()
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [node_0]
    node_1 = module_1.Node(successors=node_0, outgoing_nodes=list_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "node.Node"
    )
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.outgoing_nodes) == 1
    dict_0 = {node_1: node_0}
    var_0 = module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    var_0 = module_1.Node()
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == []
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []
    node_0 = module_1.Node(var_0, incoming_nodes=var_0, outgoing_nodes=var_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert (
        f"{type(node_0.value).__module__}.{type(node_0.value).__qualname__}"
        == "node.Node"
    )
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert (
        f"{type(node_0.incoming_nodes).__module__}.{type(node_0.incoming_nodes).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(node_0.outgoing_nodes).__module__}.{type(node_0.outgoing_nodes).__qualname__}"
        == "node.Node"
    )
    list_0 = [node_0]
    var_1 = module_0.topological_ordering(list_0)
    node_1 = module_1.Node(successor=var_0, successors=var_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert (
        f"{type(node_1.successor).__module__}.{type(node_1.successor).__qualname__}"
        == "node.Node"
    )
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "node.Node"
    )
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    var_2 = module_0.topological_ordering(tuple_0)
    module_0.topological_ordering(node_1)


def test_case_5():
    tuple_0 = ()
    node_0 = module_1.Node(successors=tuple_0, predecessors=tuple_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == ()
    assert node_0.predecessors == ()
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [node_0, node_0, node_0]
    node_1 = module_1.Node(successors=node_0, outgoing_nodes=list_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "node.Node"
    )
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert (
        f"{type(node_1.outgoing_nodes).__module__}.{type(node_1.outgoing_nodes).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.outgoing_nodes) == 3
    dict_0 = {node_1: node_0}
    var_0 = module_0.topological_ordering(dict_0)