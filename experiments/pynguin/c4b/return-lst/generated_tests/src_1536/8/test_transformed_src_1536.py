# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1536 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1316
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    bool_1 = False
    dict_0 = {bool_1: bool_1}
    str_0 = "1xsuy</1 Zp"
    tuple_0 = (bool_0, dict_0, str_0)
    list_0 = [bool_0, tuple_0, dict_0, bool_1]
    list_1 = [bool_0, list_0, dict_0, dict_0]
    var_0 = module_0.func(*list_1)
    none_type_0 = None
    list_2 = [none_type_0, none_type_0, none_type_0]
#    module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0]
    list_1 = [list_0, list_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xcdm\xfc\xdf\x89\x11\x10\xa5\xa9\x8bQap\x0b\xab"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()