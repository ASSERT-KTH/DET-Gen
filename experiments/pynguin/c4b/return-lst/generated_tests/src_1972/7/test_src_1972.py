# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1972 as module_0


def test_case_0():
    str_0 = "_0\r\r7 eI&APvw`"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "_0\r\rh eI&APvw`"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "_0\r\rih eI&j\tvwl`"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "_0\r\rih eI%uj\tvll`I"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "0\r[ih eI\x0bl&j\tfzl`oIZ"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
