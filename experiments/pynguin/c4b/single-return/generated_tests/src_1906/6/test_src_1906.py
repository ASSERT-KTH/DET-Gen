# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1906 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ";;"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\r2J.vE'VIE2f>Vs9u\"0\\"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()
