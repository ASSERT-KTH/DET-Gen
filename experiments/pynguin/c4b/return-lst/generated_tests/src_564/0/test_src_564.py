# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_564 as module_0


def test_case_0():
    str_0 = "-R<$R"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = " 0:lxBHC%hY#"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "A]?nr999oRzt\\^p\x0c\tB/"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "A]?nr999oz(\\^p\x0chB/"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [list_0, str_0, list_0]
    var_0 = module_0.func(*list_1)


def test_case_5():
    str_0 = "A]?nr999oz(\\^p\x0chB/"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0, str_0, str_0, var_0, str_0, str_0]
    list_1 = [list_0, str_0, list_0]
    var_1 = module_0.func(*list_1)


def test_case_6():
    str_0 = "A]?nr999oz(\\^p\x0chB/"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, var_0, str_0, str_0]
    list_1 = [list_0, str_0, list_0]
    var_1 = module_0.func(*list_1)