# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2426 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "9#\r['T"
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0*\x0bI"
    var_0 = module_0.func(*str_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9\x0b4"
    list_0 = [str_0]
#    module_0.func(*list_0)


def test_case_4():
    str_0 = "984"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)


def test_case_5():
    str_0 = "7\x0b7"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_6():
    str_0 = "7\x0c3\n7"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_7():
    str_0 = "7\x0c3\n4"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "7\x0c3\n1"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()