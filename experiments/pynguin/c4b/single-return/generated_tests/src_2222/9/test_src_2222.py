# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2222 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "{XG5"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "s{9Ge("
    list_0 = [str_0, str_0, str_0]
    list_1 = [str_0, str_0, str_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "@[L\r$Qs>j\nA/\tT3`af"
    list_0 = [str_0, str_0, str_0]
    list_1 = [str_0, str_0, str_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "WTK/(!xH\x0b|_5E"
    list_0 = [str_0, str_0, str_0]
    list_1 = [str_0, str_0, str_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    module_0.func()