# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2347 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ")"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
#    module_0.func(*set_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "x\rJt?QY<y&:Qz@"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_3():
    complex_0 = 495 - 896.3936748462019j
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    float_0 = -535.27283
    list_1 = [complex_0, float_0, float_0, complex_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)
    var_3 = module_0.func(*var_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ""
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()
