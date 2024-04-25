# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.breadth_first_search(bool_0, bool_0)
    assert var_0 is True


def test_case_1():
    bool_0 = True
    node_0 = module_1.Node(predecessors=bool_0, incoming_nodes=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors is True
    assert node_0.incoming_nodes is True
    assert node_0.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_0, bool_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "ir\x0cJH8k/"
    node_0 = module_1.Node(successors=str_0, outgoing_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "ir\x0cJH8k/"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == "ir\x0cJH8k/"
    module_0.breadth_first_search(node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "="
    node_0 = module_1.Node(successors=str_0, outgoing_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "="
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == "="
    list_0 = [node_0, node_0, node_0, node_0]
    node_1 = module_1.Node(successor=str_0, successors=list_0, outgoing_nodes=str_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor == "="
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.successors) == 4
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == "="
    bool_0 = True
    module_0.breadth_first_search(node_1, bool_0)