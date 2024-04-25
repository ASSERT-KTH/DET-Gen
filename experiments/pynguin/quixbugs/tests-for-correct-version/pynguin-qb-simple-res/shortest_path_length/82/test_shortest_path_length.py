# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1
import heapq as module_2


def test_case_0():
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, none_type_0, none_type_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "_W:2"
    module_0.get(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\x0c"
    node_0 = module_1.Node(successors=str_0, incoming_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "\x0c"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == "\x0c"
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(node_0, node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    module_0.get(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "upS|V9>"
    set_0 = {str_0, str_0, str_0}
    module_0.shortest_path_length(set_0, str_0, set_0)


def test_case_5():
    str_0 = ""
    node_0 = module_1.Node(successors=str_0, incoming_nodes=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == ""
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == ""
    assert node_0.outgoing_nodes == []
    var_0 = module_0.shortest_path_length(node_0, node_0, str_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    var_0 = module_2.merge()
    var_1 = module_0.get(var_0, var_0)
    assert var_1 == 0
    node_0 = module_1.Node(
        predecessors=var_1, incoming_nodes=var_0, outgoing_nodes=var_1
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == 0
    assert (
        f"{type(node_0.incoming_nodes).__module__}.{type(node_0.incoming_nodes).__qualname__}"
        == "builtins.generator"
    )
    assert node_0.outgoing_nodes == 0
    var_2 = module_0.shortest_path_length(var_1, node_0, var_1)
    assert var_2 == pytest.approx(1e309, abs=0.01, rel=0.01)
    dict_0 = {var_2: var_2, var_1: node_0}
    module_0.insert_or_update(var_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    float_0 = -751.10017
    list_0 = [float_0, float_0]
    module_0.insert_or_update(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    var_0 = module_2.merge()
    var_1 = module_0.get(var_0, var_0)
    assert var_1 == 0
    node_0 = module_1.Node(
        predecessors=var_1, incoming_nodes=var_1, outgoing_nodes=var_1
    )
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == 0
    assert node_0.incoming_nodes == 0
    assert node_0.outgoing_nodes == 0
    var_2 = module_0.shortest_path_length(var_0, node_0, var_0)
    assert var_2 == pytest.approx(1e309, abs=0.01, rel=0.01)
    tuple_0 = (node_0, node_0)
    dict_0 = {tuple_0: tuple_0, var_0: node_0, var_1: var_2}
    module_0.get(dict_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    bytes_0 = b"6\x11"
    none_type_0 = None
    var_0 = module_0.shortest_path_length(bytes_0, none_type_0, none_type_0)
    assert var_0 == 0
    dict_0 = {bytes_0: bytes_0, var_0: bytes_0}
    module_0.insert_or_update(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    str_0 = "\x0c]"
    tuple_0 = (str_0,)
    module_0.insert_or_update(tuple_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = "]"
    bool_0 = True
    tuple_0 = (str_0, bool_0)
    dict_0 = {tuple_0: str_0, tuple_0: tuple_0, str_0: tuple_0}
    var_0 = module_0.get(dict_0, bool_0)
    assert var_0 == "]"
    str_1 = "\x0c"
    node_0 = module_1.Node(successors=str_1, incoming_nodes=str_1)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "\x0c"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == "\x0c"
    assert node_0.outgoing_nodes == []
    node_1 = module_1.Node(incoming_nodes=str_1)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert node_1.value is None
    assert node_1.successor is None
    assert node_1.successors == []
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == "\x0c"
    assert node_1.outgoing_nodes == []
    node_2 = module_1.Node(outgoing_nodes=node_1)
    assert f"{type(node_2).__module__}.{type(node_2).__qualname__}" == "node.Node"
    assert node_2.value is None
    assert node_2.successor is None
    assert node_2.successors == []
    assert node_2.predecessors == []
    assert node_2.incoming_nodes == []
    assert (
        f"{type(node_2.outgoing_nodes).__module__}.{type(node_2.outgoing_nodes).__qualname__}"
        == "node.Node"
    )
    var_1 = module_0.shortest_path_length(node_2, node_2, node_0)
    assert var_1 == pytest.approx(1e309, abs=0.01, rel=0.01)
    none_type_0 = None
    module_0.shortest_path_length(node_1, node_0, none_type_0)