# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    bytes_0 = b"\xb6R\xd6q"
    var_0 = module_0.shortest_path_length(bytes_0, bytes_0, bytes_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd1dl>\xbc)\xc9\x0b"
    module_0.get(bytes_0, bytes_0)


def test_case_2():
    str_0 = ""
    var_0 = module_0.get(str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    none_type_0 = None
    module_0.shortest_path_length(bool_0, none_type_0, bool_0)


def test_case_4():
    none_type_0 = None
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    var_0 = module_0.shortest_path_length(none_type_0, node_0, none_type_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "=8"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.insert_or_update(list_0, str_0)
    node_0 = module_1.Node(successor=var_0, successors=list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == ["=8", "=8", "=8"]
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(var_0, node_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "=8"
    list_0 = [str_0, str_0, str_0]
    node_0 = module_1.Node(successor=str_0, successors=list_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == "=8"
    assert node_0.successors == ["=8", "=8", "=8"]
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(list_0, node_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, bool_0, bool_0)
    assert var_0 == 0
    list_0 = [bool_0, bool_0]
    complex_0 = -1367.20167 + 868.3771j
    tuple_0 = (list_0, list_0, complex_0)
    module_0.get(tuple_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bool_0 = False
    var_0 = module_0.shortest_path_length(bool_0, bool_0, bool_0)
    assert var_0 == 0
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0, var_0, var_0)
    var_1 = module_0.get(tuple_0, var_0)
    assert var_1 is False
    bytes_0 = b"\xdb"
    set_0 = {bytes_0, bytes_0, bytes_0}
    module_0.get(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "=8"
    var_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert var_0 == 0
    list_0 = []
    var_1 = module_0.insert_or_update(list_0, str_0)
    node_0 = module_1.Node(successor=var_1, successors=var_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == 0
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    node_1 = module_1.Node(predecessors=var_1)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert node_1.successors == []
    assert node_1.predecessors is None
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    module_0.shortest_path_length(node_1, node_0, node_1)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bytes_0 = b"\x84\xa8\xff\xc3\x1b\xfc[\x10}m\x86\x00X\xa8\xf7\x00\x1f"
    var_0 = module_0.shortest_path_length(bytes_0, bytes_0, bytes_0)
    assert var_0 == 0
    int_0 = 1
    tuple_0 = (int_0,)
    tuple_1 = (bytes_0, tuple_0)
    dict_0 = {tuple_1: int_0, int_0: tuple_0}
    module_0.insert_or_update(dict_0, dict_0)