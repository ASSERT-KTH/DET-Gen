# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"8k9\xa2\xa1+\rI\xb5Q\xf5"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    dict_0 = {var_0: var_0}
    module_0.knapsack(var_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.knapsack(bool_0, bool_0)


def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0, list_0, list_0)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    tuple_0 = (list_0, list_0, list_0)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 1
    var_1 = module_0.knapsack(bool_0, tuple_0)
    assert var_1 == 1
    bytes_0 = b"\x0f3"
    tuple_1 = (bytes_0,)
    var_2 = module_0.knapsack(bool_0, tuple_1)
    assert var_2 == 0
    module_1.object(*var_1)