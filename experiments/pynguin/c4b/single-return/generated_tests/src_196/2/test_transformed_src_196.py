# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_196 as module_0


def test_case_0():
    int_0 = 2064
    dict_0 = {int_0: int_0}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0 0 0 0"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "!"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0 0 0"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "In?d=?s& _\rJCX0-O>!@"
    list_0 = [str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "! 8 0 0"
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)
