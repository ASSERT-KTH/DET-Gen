# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"9tU\x99\xb4\x18tt\xfa\x14\x04#\xa9\x04"
    set_0 = set()
    var_0 = module_0.knapsack(bytes_0, set_0)
    assert var_0 == 0
    module_0.knapsack(var_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -275.439328
    none_type_0 = None
    module_0.knapsack(float_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b"\x92\xdb"
    tuple_0 = (bytes_0, bool_0)
    module_0.knapsack(bool_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bytes_0 = b"\x90\x0c"
    tuple_0 = (bytes_0, bool_0)
    int_0 = 4154
    module_0.knapsack(int_0, tuple_0)
