# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xe4\xee*TQ\x1e\x01\xcdn\xff\xff\xe4\xf0YH!z"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.knapsack(str_0, str_0)
    assert var_0 == 0
    bytes_0 = b"\xe4\xee*TQ\x1e\x01\xcdn\xff\xff\xe4\xf0YH!z"
    module_0.knapsack(bytes_0, bytes_0)


def test_case_2():
    str_0 = ""
    var_0 = module_0.knapsack(str_0, str_0)
    assert var_0 == 0
    dict_0 = {var_0: var_0, str_0: var_0, var_0: var_0}
    tuple_0 = (dict_0,)
    var_1 = module_0.knapsack(var_0, tuple_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ""
    var_0 = module_0.knapsack(str_0, str_0)
    assert var_0 == 0
    dict_0 = {var_0: var_0, str_0: str_0, var_0: var_0}
    tuple_0 = (dict_0,)
    bool_0 = True
    module_0.knapsack(bool_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 624
    list_0 = [int_0, int_0]
    tuple_0 = (list_0,)
    var_0 = module_0.knapsack(int_0, tuple_0)
    assert var_0 == 624
    bool_0 = False
    module_1.object(*bool_0, **bool_0)