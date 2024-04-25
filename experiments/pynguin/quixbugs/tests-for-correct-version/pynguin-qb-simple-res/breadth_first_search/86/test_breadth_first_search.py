# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    bytes_0 = b"\xd5\xb0\x93\xfd\xb2\xb7\x01E9u;\xd2\xdb)\xbeA\xa8\xd8<"
    var_0 = module_0.breadth_first_search(bytes_0, bytes_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    set_0 = set()
    module_0.breadth_first_search(none_type_0, set_0)


def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(none_type_0, none_type_0, predecessors=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_0, none_type_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'u{)6=["<Y.]J'
    node_0 = module_1.Node(successors=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == 'u{)6=["<Y.]J'
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.breadth_first_search(node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "C"
    node_0 = module_1.Node(str_0, str_0, str_0, outgoing_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == "C"
    assert node_0.successor == "C"
    assert node_0.successors == "C"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == "C"
    set_0 = {node_0, str_0}
    node_1 = module_1.Node(successors=set_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.set"
    )
    assert len(node_1.successors) == 2
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    var_0 = module_0.breadth_first_search(node_1, str_0)
    assert var_0 is True
    node_2 = module_1.Node(incoming_nodes=var_0)
    assert f"{type(node_2).__module__}.{type(node_2).__qualname__}" == "node.Node"
    assert node_2.value is None
    assert node_2.successor is None
    assert node_2.successors == []
    assert node_2.predecessors == []
    assert node_2.incoming_nodes is True
    assert node_2.outgoing_nodes == []
    node_2.successors()