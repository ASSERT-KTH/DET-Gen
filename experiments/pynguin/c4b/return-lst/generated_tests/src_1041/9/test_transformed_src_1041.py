# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1041 as module_0


def test_case_0():
    str_0 = "+n"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "+n"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "n?_cU_{[!1//_dD/"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "L?B_cU[\x0c{!!1//_dr"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "L?cU\x0c{!!1///_\\r"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)