# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"~@\xe2(\xcf\x13\xb8\x9a}c\x03\x8e"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 4095
#    module_0.func()


def test_case_1():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1Q3w*@"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "0i\rF@h]NVk?7N"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = -466.652
    str_0 = '>s\tR~j&b/"j'
    list_0 = [float_0, str_0]
    list_1 = [list_0, float_0, float_0]
#    module_0.func(*list_1)
