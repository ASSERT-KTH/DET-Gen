# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1412.8
    complex_0 = -418.3564 - 1201.88j
    dict_0 = {float_0: complex_0, complex_0: float_0}
    module_0.knapsack(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.knapsack(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    bytes_0 = b"\x97\xb7"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    bool_0 = False
    dict_0 = {tuple_0: bool_0, bool_0: bool_0, bool_0: bool_0, tuple_0: bool_0}
    tuple_1 = (dict_0, tuple_0, bool_0, bool_0)
    module_0.knapsack(bool_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    bool_0 = True
    dict_0 = {
        bool_0: tuple_0,
        tuple_0: bool_0,
        bool_0: bool_0,
        bool_0: bool_0,
        tuple_0: bool_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
    }
    tuple_1 = (dict_0, tuple_0, bool_0, bool_0)
    module_0.knapsack(bool_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    int_0 = 397
    bytes_0 = b"(\x07"
    tuple_0 = (bytes_0, bool_0)
    module_0.knapsack(int_0, tuple_0)
