# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_402 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "0.\n\rvbX#NR%"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


def test_case_2():
    int_0 = -1832
    bytes_0 = b""
    tuple_0 = (int_0, int_0, int_0, bytes_0)
    list_0 = [int_0, bytes_0, tuple_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    int_0 = -197
    module_1.object(**int_0)
