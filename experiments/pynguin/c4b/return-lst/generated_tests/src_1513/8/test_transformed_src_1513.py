# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1513 as module_0
import builtins as module_1


def test_case_0():
    float_0 = -3447.74
    list_0 = [float_0, float_0]
    bytes_0 = b"\x18G\xb2Vte\xf2\xbeP\x18\x0e\x85Y\xb8\x98N\xef9$5"
    set_0 = {bytes_0, float_0}
    tuple_0 = (list_0, bytes_0, set_0, float_0)
    list_1 = [tuple_0, list_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "5l9@zdU,9tFFrMxY"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*var_0, **var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "5lHdU,9tfF2r5xY"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "MQGl|sw\"j-I#CFf'73I("
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
#    module_1.object(*str_0, **var_0)
