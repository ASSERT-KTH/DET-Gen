# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1780 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "n)(H"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "n)(H"
    var_0 = module_0.func(*str_0)


def test_case_3():
    str_0 = "{V\\"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "vVK"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "KK"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, list_0]
    var_1 = module_0.func(*list_1)


def test_case_6():
    str_0 = "VV"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    list_1 = [list_0, var_1]
    var_2 = module_0.func(*list_1)
    var_3 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "VVVK"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    list_1 = [list_0, var_1]
    var_2 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "KKK"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)
