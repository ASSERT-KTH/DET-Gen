# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    str_0 = "e/t0T&n=B!lM[M&1!"
    node_0 = module_0.shortest_path_length(str_0, str_0, str_0)
    assert node_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "mc1.q/HzaL"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    module_0.get(dict_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 859.0018
    list_0 = [float_0, float_0, float_0]
    module_0.shortest_path_length(list_0, float_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "e/0TMn=B}?h!l[M&1F"
    node_0 = module_1.Node(successors=str_0, predecessors=str_0)
    module_0.shortest_path_length(node_0, node_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "[F"
    module_0.insert_or_update(str_0, str_0)


def test_case_5():
    str_0 = "e/t0TMn=Bh!lM[M&1F"
    node_0 = module_1.Node()
    var_0 = module_0.shortest_path_length(node_0, node_0, str_0)
    assert var_0 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\xbaI\xda\xe9Q\xa9"
    bool_0 = True
    set_0 = {bytes_0, bool_0}
    tuple_0 = (set_0, bool_0, set_0, set_0)
    str_0 = "{PUA-"
    module_0.get(tuple_0, str_0)


def test_case_7():
    bytes_0 = b"\xbaI\xda\xe9Q\xa9"
    bool_0 = True
    set_0 = {bytes_0, bool_0}
    tuple_0 = (set_0, bool_0, set_0, set_0)
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, bool_0, bool_0)
    assert var_0 == 0
    var_1 = module_0.get(tuple_0, bytes_0)
    assert var_1 is True


def test_case_8():
    list_0 = []
    str_0 = "#Q"
    var_0 = module_0.insert_or_update(list_0, str_0)
    var_1 = module_0.get(list_0, str_0)
    assert var_1 == 0
    node_0 = module_1.Node(incoming_nodes=var_0)
    node_1 = module_1.Node(incoming_nodes=var_1)
    assert node_1.incoming_nodes == 0
    var_2 = module_0.shortest_path_length(var_1, node_0, var_1)
    assert var_2 == pytest.approx(1e309, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_9():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    bytes_0 = b"\xbaI\xda\xe9Q\xff$\xa9"
    tuple_1 = (tuple_0, bytes_0)
    module_0.insert_or_update(tuple_1, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    list_0 = []
    var_0 = module_0.shortest_path_length(list_0, list_0, list_0)
    assert var_0 == 0
    str_0 = "#Q"
    var_1 = module_0.insert_or_update(list_0, str_0)
    str_1 = "e/t0TMn=B!lM[M&1F"
    var_2 = module_0.insert_or_update(list_0, str_0)
    var_3 = module_0.get(list_0, str_0)
    assert var_3 == 0
    dict_0 = {
        str_1: str_1,
        str_1: str_1,
        str_1: str_1,
        var_2: var_0,
        str_1: str_1,
        str_1: str_1,
        str_1: str_1,
        var_2: var_2,
    }
    module_0.insert_or_update(list_0, dict_0)
