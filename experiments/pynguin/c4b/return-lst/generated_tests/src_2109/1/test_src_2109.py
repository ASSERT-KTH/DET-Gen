# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2109 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "#c/d6JS]X"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "=7QBb47'Gu"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    str_0 = "=7b477Gu"
    list_0 = [str_0, none_type_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    str_0 = "xC7b477GDI447|"
    list_0 = [str_0, none_type_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()