# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import node as module_0
import topological_ordering as module_1


def test_case_0():
    node_0 = module_0.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    list_0 = [node_0, node_0, node_0]
    var_0 = module_1.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    node_0 = module_0.Node(successor=bool_0, predecessors=bool_0, incoming_nodes=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is True
    assert node_0.successors == []
    assert node_0.predecessors is True
    assert node_0.incoming_nodes is True
    assert node_0.outgoing_nodes == []
    module_1.topological_ordering(node_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa60L\xfe\xfa\x13"
    none_type_0 = None
    node_0 = module_0.Node(
        bytes_0, none_type_0, predecessors=bytes_0, incoming_nodes=bytes_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == b"\xa60L\xfe\xfa\x13"
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == b"\xa60L\xfe\xfa\x13"
    assert node_0.incoming_nodes == b"\xa60L\xfe\xfa\x13"
    assert node_0.outgoing_nodes == []
    set_0 = {node_0, node_0}
    var_0 = module_1.topological_ordering(set_0)
    node_0.successor()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa60?\xc5\x13"
    none_type_0 = None
    node_0 = module_0.Node(
        successor=none_type_0,
        successors=bytes_0,
        predecessors=none_type_0,
        incoming_nodes=none_type_0,
        outgoing_nodes=bytes_0,
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == b"\xa60?\xc5\x13"
    assert node_0.predecessors is None
    assert node_0.incoming_nodes is None
    assert node_0.outgoing_nodes == b"\xa60?\xc5\x13"
    set_0 = {node_0, node_0}
    module_1.topological_ordering(set_0)