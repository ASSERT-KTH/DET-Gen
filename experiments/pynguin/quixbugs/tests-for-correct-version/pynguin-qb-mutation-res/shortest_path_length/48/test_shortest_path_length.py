# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_path_length as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, none_type_0, none_type_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xc8\x1d"
    dict_0 = {bytes_0: bytes_0}
    var_0 = module_0.insert_or_update(dict_0, bytes_0)
    module_0.get(bytes_0, var_0)


def test_case_2():
    tuple_0 = ()
    var_0 = module_0.get(tuple_0, tuple_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 425.9
    module_0.insert_or_update(float_0, float_0)


def test_case_4():
    node_0 = module_1.Node()
    var_0 = module_0.shortest_path_length(node_0, node_0, node_0)
    assert var_0 == 0
    var_1 = module_0.shortest_path_length(var_0, node_0, var_0)
    assert var_1 == pytest.approx(1e309, abs=0.01, rel=0.01)


def test_case_5():
    bytes_0 = b"\xc8\x1d"
    dict_0 = {bytes_0: bytes_0}
    var_0 = module_0.insert_or_update(dict_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    tuple_0 = ()
    int_0 = 1285
    tuple_1 = (tuple_0, int_0)
    list_0 = [tuple_1, tuple_1, tuple_0]
    var_0 = module_0.get(list_0, int_0)
    module_0.shortest_path_length(var_0, list_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    module_0.insert_or_update(tuple_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    bytes_0 = b"\xc8\x1d"
    dict_0 = {bytes_0: bytes_0}
    none_type_0 = None
    var_0 = module_0.get(dict_0, none_type_0)
    assert var_0 == 0
    var_1 = module_0.insert_or_update(dict_0, bytes_0)
    module_0.shortest_path_length(bytes_0, dict_0, var_1)


@pytest.mark.xfail(strict=True)
def test_case_9():
    none_type_0 = None
    var_0 = module_0.shortest_path_length(none_type_0, none_type_0, none_type_0)
    assert var_0 == 0
    bytes_0 = b"\xc8\x1d"
    dict_0 = {bytes_0: bytes_0}
    none_type_1 = None
    var_1 = module_0.get(dict_0, dict_0)
    assert var_1 == 0
    var_2 = module_0.get(dict_0, none_type_1)
    assert var_2 == 0
    var_3 = module_0.shortest_path_length(var_1, none_type_1, none_type_1)
    assert var_3 == 0
    var_4 = module_0.insert_or_update(dict_0, bytes_0)
    module_0.insert_or_update(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_10():
    bytes_0 = b"\xd4K\xd0\xe7e^\x02Y\x1d\xf1&="
    node_0 = module_1.Node(successors=bytes_0)
    module_0.shortest_path_length(node_0, node_0, bytes_0)