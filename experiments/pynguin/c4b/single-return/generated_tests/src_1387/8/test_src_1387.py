# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1387 as module_0


def test_case_0():
    int_0 = 861
    set_0 = {int_0, int_0}
    list_0 = [set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "UY%^8T/{^M}"
    set_0 = {str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "jJ"
    set_0 = {str_0}
    tuple_0 = (str_0, str_0, set_0)
    list_0 = [tuple_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*set_0)
    assert var_1 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ")w8 8a.6_i]O>Vf=U<hD"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
    tuple_0 = (var_0, str_0, var_0)
    list_0 = [tuple_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "YES"
    var_2 = module_0.func(*var_1)
    assert var_2 == "YES"
    module_0.func()
