# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xaem%NJ:\xdf\xcf\xc3#\xf8r\xed\xcbH"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.knapsack(str_0, str_0)
    assert var_0 == 0
    module_0.knapsack(var_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\x83b"
    tuple_0 = (bytes_0, bool_0, bool_0)
    module_0.knapsack(bool_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bytes_0 = b"\x00J"
    tuple_0 = (bytes_0, bool_0, bool_0)
    module_0.knapsack(bool_0, tuple_0)