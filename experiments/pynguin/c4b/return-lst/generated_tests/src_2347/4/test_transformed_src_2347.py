# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2347 as module_0


def test_case_0():
    bool_0 = True
    set_0 = {bool_0}
    tuple_0 = (bool_0, bool_0, set_0)
    bytes_0 = b"\xde4U\xa8c\x15b\xfd\xb5p"
    tuple_1 = (tuple_0, bool_0, bytes_0)
    var_0 = module_0.func(*tuple_1)


def test_case_1():
    str_0 = ""
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -1902.0
    float_1 = 3174.07743
    dict_0 = {float_0: float_0, float_0: float_1, float_0: float_1}
    var_0 = module_0.func(*dict_0)
#    module_0.func()