# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xab B\xc6\xbd\x0c\xcc\xc0\x19"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.knapsack(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 4650
    module_0.knapsack(int_0, int_0)


def test_case_3():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    str_0 = "c="
    list_0 = [str_0]
    var_1 = module_0.knapsack(var_0, list_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "~="
    list_0 = [str_0, str_0, str_0]
    bool_0 = False
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 0
    int_0 = 3964
    module_0.knapsack(int_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "v="
    list_0 = [str_0, str_0, str_0, str_0]
    bool_0 = False
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 0
    int_0 = 3937
    bytes_0 = b"\xafr"
    str_1 = "S\x0b-,0!=t;^CJ9Vks`z"
    tuple_0 = (bytes_0, bool_0, var_0, str_1)
    module_0.knapsack(int_0, tuple_0)