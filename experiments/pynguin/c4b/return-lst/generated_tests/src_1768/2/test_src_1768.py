# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1768 as module_0


def test_case_0():
    str_0 = "`FpW;o0nK"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0)
    list_0 = [tuple_0, tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "`FpW;o0nK"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "z=G"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "R="
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "z=6"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()