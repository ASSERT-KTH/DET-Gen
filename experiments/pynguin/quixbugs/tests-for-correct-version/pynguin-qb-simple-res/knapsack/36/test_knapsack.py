# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    tuple_1 = (tuple_0, bool_0)
    module_0.knapsack(bool_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    var_1 = module_0.knapsack(tuple_0, tuple_0)
    assert var_1 == 0
    module_0.knapsack(tuple_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -2141.1477
    module_0.knapsack(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xca\x9c"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    bool_0 = True
    var_0 = module_0.knapsack(bool_0, list_0)
    assert var_0 == 0
    module_1.object(*list_0)