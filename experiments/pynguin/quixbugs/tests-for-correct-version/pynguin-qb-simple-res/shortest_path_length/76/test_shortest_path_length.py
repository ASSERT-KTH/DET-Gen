# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    int_0 = -368
    var_0 = module_0.shortest_path_length(int_0, int_0, int_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    none_type_0 = None
    module_0.get(dict_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    bool_0 = True
    module_0.shortest_path_length(none_type_0, none_type_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -824.9478246241615
    set_0 = {float_0, float_0, float_0}
    list_0 = []
    var_0 = module_0.get(list_0, float_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(set_0, float_0, float_0)
    assert var_1 == 0
    none_type_0 = None
    bool_0 = True
    module_0.shortest_path_length(none_type_0, bool_0, var_1)


def test_case_4():
    list_0 = []
    tuple_0 = (list_0, list_0)
    var_0 = module_0.insert_or_update(list_0, tuple_0)
    var_1 = module_0.insert_or_update(list_0, tuple_0)


def test_case_5():
    int_0 = 1579
    node_0 = module_1.Node(successor=int_0, predecessors=int_0, outgoing_nodes=int_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == 1579
    assert node_0.successors == []
    assert node_0.predecessors == 1579
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == 1579
    var_0 = module_0.shortest_path_length(node_0, node_0, int_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    list_0 = []
    var_0 = module_0.get(list_0, list_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(list_0, var_0, var_0)
    assert var_1 == 0
    float_0 = -471.0
    tuple_0 = (float_0, float_0)
    var_2 = module_0.insert_or_update(list_0, tuple_0)
    var_3 = module_0.get(list_0, var_1)
    assert var_3 == 0
    module_0.shortest_path_length(var_1, var_2, var_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    list_0 = []
    none_type_0 = None
    var_0 = module_0.get(list_0, none_type_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(list_0, none_type_0, none_type_0)
    assert var_1 == 0
    tuple_0 = (none_type_0, none_type_0)
    var_2 = module_0.insert_or_update(list_0, tuple_0)
    var_3 = module_0.get(list_0, none_type_0)
    bool_0 = True
    module_0.shortest_path_length(bool_0, var_3, var_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "?u\t\x0cvC)\t\x0c+g\x0b!b"
    node_0 = module_1.Node(successors=str_0, predecessors=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == "?u\t\x0cvC)\t\x0c+g\x0b!b"
    assert node_0.predecessors == "?u\t\x0cvC)\t\x0c+g\x0b!b"
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.shortest_path_length(str_0, node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    list_0 = []
    none_type_0 = None
    var_0 = module_0.get(list_0, none_type_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(list_0, none_type_0, none_type_0)
    assert var_1 == 0
    tuple_0 = (none_type_0, none_type_0)
    var_2 = module_0.insert_or_update(list_0, tuple_0)
    node_0 = module_1.Node(successor=var_0, successors=list_0, incoming_nodes=var_1)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor == 0
    assert node_0.successors == [(None, None)]
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == 0
    assert node_0.outgoing_nodes == []
    set_0 = {node_0, node_0, var_1}
    module_0.insert_or_update(list_0, set_0)