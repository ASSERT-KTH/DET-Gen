# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2086 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa9\x8a\x82*\x87E)\xd9"
    var_0 = module_0.func(*bytes_0)
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
#    module_0.func(*list_0)


def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 3153.0
    list_0 = [float_0, float_0, float_0]
    str_0 = "2P!"
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
#    module_0.func()
