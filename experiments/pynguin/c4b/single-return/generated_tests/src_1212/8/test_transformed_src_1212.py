# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1212 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "@TIZ6(3.UefrE"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 151
    bytes_0 = b"X|~\xc5"
    bool_0 = True
    float_0 = -2819.72
    tuple_0 = (int_0, bytes_0, bool_0, float_0)
    list_0 = [tuple_0, bytes_0, bytes_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "dCvV>MmF"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    list_1 = [list_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ':*{.U*{A9\r}jU]0_G/"'
    tuple_0 = (str_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "NO"
    dict_0 = module_0.func(*var_0)
    assert dict_0 == "YES"
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "YES"
    var_2 = module_0.func(*list_0)
    assert var_2 == "YES"
#    module_0.func()
