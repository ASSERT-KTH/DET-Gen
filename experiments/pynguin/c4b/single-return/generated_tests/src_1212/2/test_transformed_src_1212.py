# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1212 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"G\xb1"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1613.81
    dict_0 = {float_0: float_0, float_0: float_0}
    list_0 = [dict_0, dict_0, dict_0, float_0]
    bytes_0 = b"\xae\xd3"
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    list_1 = [bytes_0, bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1613.81
    dict_0 = {float_0: float_0, float_0: float_0}
    list_0 = [dict_0, dict_0, dict_0, float_0]
    tuple_0 = (float_0, dict_0, list_0, dict_0)
    bool_0 = False
    tuple_1 = (tuple_0, float_0, bool_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == "NO"
    bytes_0 = b"\xae\xd3"
    list_1 = [bytes_0, bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
#    module_0.func()
