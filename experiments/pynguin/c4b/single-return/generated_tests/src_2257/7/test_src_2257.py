# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2257 as module_0


def test_case_0():
    str_0 = "LX3sf"
    var_0 = module_0.func(*str_0)
    assert var_0 == "l"


def test_case_1():
    str_0 = "LX3sf"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "LX3sf"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '"}!LX3s'
    var_0 = module_0.func(*str_0)
    assert var_0 == '"'
    module_0.func()


def test_case_4():
    str_0 = "LX3"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "lx3"
