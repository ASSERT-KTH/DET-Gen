# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_91 as module_0


def test_case_0():
    str_0 = "dV`DLX?wa9*-_5Ra4"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ",88]=Hv"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 5
    module_0.func(*var_0)


def test_case_3():
    str_0 = "hl'"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "a~hl'"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "h1i"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    module_0.func()