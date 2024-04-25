# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    str_0 = ""
    var_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_0 == 0


def test_case_1():
    list_0 = []
    none_type_0 = None
    node_0 = module_1.Node(list_0, list_0, list_0, none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value == []
    assert node_0.successor == []
    assert node_0.successors == []
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    set_0 = {node_0, node_0, none_type_0}
    list_1 = [set_0, node_0, set_0, list_0]
    var_0 = module_0.get(list_1, none_type_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value == []
    assert var_0.successor == []
    assert var_0.successors == []
    assert var_0.predecessors is None
    assert var_0.incoming_nodes == []
    assert var_0.outgoing_nodes == []


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '4Z\\{ kz"]F>)Mx '
    node_0 = module_1.Node(successor=str_0, successors=str_0, incoming_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == '4Z\\{ kz"]F>)Mx '
    assert node_0.successors == '4Z\\{ kz"]F>)Mx '
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == '4Z\\{ kz"]F>)Mx '
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(node_0, node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.insert_or_update(none_type_0, none_type_0)


def test_case_4():
    object_0 = module_2.object()
    list_0 = [object_0, object_0]
    list_1 = [list_0]
    var_0 = module_0.insert_or_update(list_1, list_0)


def test_case_5():
    str_0 = '4Z\\{ kz"]F>)Mx '
    node_0 = module_1.Node(predecessors=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == '4Z\\{ kz"]F>)Mx '
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.shortest_path_length(str_0, node_0, str_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    set_0 = set()
    bytes_0 = b"\x98\xf0 \xcf\xb3\x99s\xa1M0\xa39M\x9e\xc8\xb3\x01]"
    tuple_0 = (bytes_0, bytes_0)
    module_0.insert_or_update(set_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"At"
    set_0 = {bytes_0, bytes_0}
    var_0 = module_0.get(set_0, bytes_0)
    assert var_0 == 0
    str_0 = '4Z\\{ kz"]F>)Mx '
    str_1 = ")^oa&R[Xs>\r9(g{F{`W"
    node_0 = module_1.Node(
        successor=str_1, successors=str_0, incoming_nodes=str_0, outgoing_nodes=str_0
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == ")^oa&R[Xs>\r9(g{F{`W"
    assert node_0.successors == '4Z\\{ kz"]F>)Mx '
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == '4Z\\{ kz"]F>)Mx '
    assert node_0.outgoing_nodes == '4Z\\{ kz"]F>)Mx '
    var_1 = module_0.shortest_path_length(str_0, node_0, node_0)
    assert var_1 == 0
    module_0.shortest_path_length(node_0, node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bytes_0 = b"\xd2\xb3"
    bool_0 = False
    tuple_0 = (bytes_0, bool_0)
    module_0.insert_or_update(tuple_0, tuple_0)