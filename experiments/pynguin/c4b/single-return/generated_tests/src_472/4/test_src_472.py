# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_472 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "XA?xP@P5d\r~>5p\nWl"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_1():
    str_0 = "XA?xP@P5d\r~>5p\nWl"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "\x0c&j"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "KV"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "b5VVBwswLgppg&';aZ|"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    var_2 = module_0.func(*list_0)
    assert var_2 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "\t#\\4wc_YKK95T\\f$Nt{"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    module_0.func()
