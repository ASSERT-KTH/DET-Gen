# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_869 as module_0


def test_case_0():
    str_0 = "c5y:q\nUxnEyUy2"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "c5y:q\nUxnEyUy2"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
#    module_0.func(*tuple_0)


def test_case_3():
    str_0 = "c5y:qUUHnyyUy2"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "/2gxSR7c$d1p c"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, list_0]
    var_1 = module_0.func(*list_1)
