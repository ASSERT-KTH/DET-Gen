# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -494
    list_0 = [int_0]
    module_0.kth(list_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x1a+\xb5"
    module_0.kth(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 947.37753
    bool_0 = True
    tuple_0 = (float_0, bool_0)
    module_0.kth(tuple_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 2998
    str_0 = "(=3kr9^#|1m]xz/j~/"
    module_0.kth(str_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    var_0 = module_0.kth(tuple_0, bool_0)
    assert var_0 is True
    module_0.kth(bool_0, var_0)