# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2116 as module_0


def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 859
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "2iU']t4B1sb]&/"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
    module_0.func()
