# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "0\n\r"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "$U\\F56%\to,jSL"
    bytes_0 = b""
    var_0 = module_0.knapsack(str_0, bytes_0)
    assert var_0 == 0
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0)
    set_0 = {bool_0, tuple_0}
    tuple_1 = (set_0,)
    module_0.knapsack(bool_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    int_0 = 776
    tuple_0 = (bool_0, bool_0, bool_0)
    set_0 = {int_0, tuple_0}
    tuple_1 = (set_0,)
    var_0 = module_0.knapsack(bool_0, tuple_1)
    assert var_0 == 0
    module_0.knapsack(int_0, var_0)
