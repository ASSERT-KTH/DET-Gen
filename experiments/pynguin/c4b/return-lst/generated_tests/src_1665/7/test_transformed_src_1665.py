# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1665 as module_0


def test_case_0():
    dict_0 = {}
    float_0 = 3101.5011
    list_0 = [dict_0, float_0, float_0, dict_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_1)


def test_case_1():
    dict_0 = {}
    float_0 = 3101.5011
    list_0 = [dict_0, float_0, float_0, dict_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    float_0 = -1701.45
    set_0 = {float_0}
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xfa\x11\x16K`k\xca\xf2\xc4\x12"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
#    module_0.func(*bytes_0)


def test_case_5():
    float_0 = -1701.45
    set_0 = {float_0}
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
