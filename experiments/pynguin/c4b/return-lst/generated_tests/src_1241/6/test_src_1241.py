# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1241 as module_0


def test_case_0():
    int_0 = -1238
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 501
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0]
    module_0.func(*list_0)


def test_case_3():
    bool_0 = True
    str_0 = "4"
    list_0 = [bool_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4"
    list_0 = [str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    str_0 = "{g"
    list_0 = [bool_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    str_0 = "4"
    tuple_0 = (bool_0,)
    str_1 = "[96fNc"
    list_0 = [str_0, tuple_0, str_0, str_1]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = True
    str_0 = "7"
    list_0 = [bool_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "7"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)