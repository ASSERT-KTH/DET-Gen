# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import find_first_in_sorted as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -89
    list_0 = [int_0, int_0, int_0]
    module_0.find_first_in_sorted(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.find_first_in_sorted(list_0, list_0)
    assert var_0 == -1
    var_1 = module_0.find_first_in_sorted(list_0, var_0)
    assert var_1 == -1
    module_0.find_first_in_sorted(var_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.find_first_in_sorted(none_type_0, none_type_0)


def test_case_3():
    int_0 = 2169
    tuple_0 = (int_0,)
    str_0 = "@OP"
    tuple_1 = (tuple_0, str_0)
    var_0 = module_0.find_first_in_sorted(tuple_1, str_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    var_0 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_0 == 0
    module_0.find_first_in_sorted(var_0, bool_0)


def test_case_5():
    bool_0 = False
    bytes_0 = b"{\x84y\xc8N\x9a\x96\xa2\xde\xcf"
    var_0 = module_0.find_first_in_sorted(bytes_0, bool_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "\\k(N6j+jBxQ"
    var_0 = module_0.find_first_in_sorted(str_0, str_0)
    assert var_0 == -1
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    var_1 = module_0.find_first_in_sorted(tuple_0, bool_0)
    assert var_1 == 0
    module_0.find_first_in_sorted(var_1, bool_0)