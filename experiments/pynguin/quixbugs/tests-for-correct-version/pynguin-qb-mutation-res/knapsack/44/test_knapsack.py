# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x0ea\xf6y\xa1\x88\x14"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    bytes_0 = b"=\x1da\xf6\xe6\xa1\x88\x14"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bool_1 = False
    dict_0 = {bool_0: bool_0, bool_1: bool_1, bool_1: bool_0, bool_1: bool_1}
    module_0.knapsack(dict_0, bool_1)


def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0,)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 662
    int_1 = -2110
    tuple_0 = (int_0, int_1)
    float_0 = -2899.672154
    tuple_1 = (tuple_0, float_0)
    module_0.knapsack(int_0, tuple_1)