# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2377 as module_0


def test_case_0():
    str_0 = '4~h!"=01y;5sbRB"'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "{/xe^a\rh(Pxel|WU\n  "
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "{/xe^a\rh(Pxep|WUo  "
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_4():
    str_0 = "{/xe^a\rh(Pxel|WU\nl  "
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "/xe^a\rh(Pxel|UOl o{"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)