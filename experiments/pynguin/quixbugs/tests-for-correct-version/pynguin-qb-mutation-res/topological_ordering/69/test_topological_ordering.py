# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    str_0 = ""
    var_0 = module_0.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"B\xbc\xc5\x89\x9d\xf2\x96\xe0\xd5\x82"
    module_0.topological_ordering(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.topological_ordering(none_type_0)


def test_case_3():
    bytes_0 = b'\xa8\xa8<:^\xc8&\xec\xc2"\xe0Z\x87\x7f[\x15'
    node_0 = module_1.Node(
        successor=bytes_0,
        predecessors=bytes_0,
        incoming_nodes=bytes_0,
        outgoing_nodes=bytes_0,
    )
    set_0 = {node_0}
    node_1 = module_1.Node(
        set_0, successors=set_0, predecessors=set_0, outgoing_nodes=set_0
    )
    tuple_0 = (node_1, node_0)
    var_0 = module_0.topological_ordering(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b""
    node_0 = module_1.Node(
        successor=bytes_0,
        predecessors=bytes_0,
        incoming_nodes=bytes_0,
        outgoing_nodes=bytes_0,
    )
    set_0 = {node_0, node_0}
    var_0 = module_0.topological_ordering(set_0)
    node_1 = module_1.Node(set_0, successors=set_0, incoming_nodes=set_0)
    node_2 = module_1.Node(
        var_0, successors=var_0, predecessors=var_0, outgoing_nodes=set_0
    )
    assert len(node_2.value) == 1
    assert len(node_2.successors) == 1
    assert len(node_2.predecessors) == 1
    tuple_0 = (node_2, node_1)
    var_1 = module_0.topological_ordering(tuple_0)
    module_0.topological_ordering(node_2)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b""
    node_0 = module_1.Node(
        successor=bytes_0,
        predecessors=bytes_0,
        incoming_nodes=bytes_0,
        outgoing_nodes=bytes_0,
    )
    set_0 = {node_0, node_0}
    var_0 = module_0.topological_ordering(set_0)
    node_1 = module_1.Node(
        var_0, successors=var_0, predecessors=var_0, outgoing_nodes=set_0
    )
    assert len(node_1.value) == 1
    assert len(node_1.successors) == 1
    assert len(node_1.predecessors) == 1
    tuple_0 = (node_1, node_0)
    var_1 = module_0.topological_ordering(tuple_0)
    module_0.topological_ordering(node_1)