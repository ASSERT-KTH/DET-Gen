# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_91 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"d^"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = '"1:{c+\x0bA,zw9)b4Q'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    var_1 = module_0.func(*list_0)
    assert var_1 == 5


def test_case_3():
    str_0 = "hXdEz#"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "a\r#"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    var_1 = module_1.object()
    module_0.func()


def test_case_5():
    str_0 = "h8dEz}"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
