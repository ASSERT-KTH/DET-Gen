# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2557 as module_0


def test_case_0():
    str_0 = "y2$3Xm6!<(tw?"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    str_0 = "\ndtUbocR{w"
    list_0 = [str_0, str_0, none_type_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*str_0)
    module_0.func()


def test_case_3():
    str_0 = "y2$3Xm6!<(tw?"
    dict_0 = {str_0: str_0}
    var_0 = module_0.func(*dict_0)


def test_case_4():
    str_0 = "6{{Xp!0hS"
    dict_0 = {str_0: str_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    none_type_0 = None
    str_0 = "\ndtUboc{"
    list_0 = [str_0, str_0, none_type_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*str_0)
    module_0.func()