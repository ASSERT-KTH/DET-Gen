# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    bool_0 = True
    set_0 = {bool_0, none_type_0}
    module_0.knapsack(none_type_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    object_0 = module_1.object(*list_0)
    var_0 = module_0.knapsack(object_0, list_0)
    assert var_0 == 0
    str_0 = "C.]^`#S"
    module_0.knapsack(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 2238.5 - 1542.0494j
    module_0.knapsack(complex_0, complex_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 980
    set_0 = set()
    var_0 = module_0.knapsack(int_0, set_0)
    assert var_0 == 0
    set_1 = {var_0, int_0}
    tuple_0 = (set_1, var_0, var_0, var_0)
    module_0.knapsack(int_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 980
    set_0 = set()
    var_0 = module_1.object()
    set_1 = {var_0, int_0}
    tuple_0 = (set_1, var_0, var_0, set_0)
    module_0.knapsack(int_0, tuple_0)