# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1389 as module_0
import builtins as module_1


def test_case_0():
    dict_0 = {}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"


def test_case_1():
    str_0 = "!gh2"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "5"


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "&|5 J9E"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "=<2/|f(NI%xc&3q7nz0"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "11"
    module_1.object(**list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "@rKnAlxV@mbrMyX@'>"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "14"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "_^\x0bF<ZGT)O@|.E"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "10"
    var_1 = module_0.func(*var_0)
    assert var_1 == "2"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "WMTY0F Q{*A nd"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "U"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    var_1 = module_0.func(*var_0)
    assert var_1 == "2"
    object_0 = module_1.object()
    module_0.func()
