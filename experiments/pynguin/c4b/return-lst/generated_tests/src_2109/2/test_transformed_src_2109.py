# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2109 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "&}X"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = '77":QH34sYJ32#f9'
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '77"4QH34sYJ32#f9'
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    object_0 = module_1.object()
    object_1 = module_1.object()
    var_1 = module_0.func(*var_0)
#    module_0.func()


def test_case_4():
    str_0 = '77"47#4\r\n734ql'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    var_1 = module_0.func(*var_0)
