# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2215 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "O<l*Mi*B]iHghD\tQ\x0ct"
#    module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc8^\xdf\x10~N\x06\xf7\x04\xf6\xbdQ\xe23\x98"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "200942231612678624742461898122651152"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0="
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xc8^\xdf\x10~N\x06\xf7\x04\xf6\xbdQ\xe23\x98"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "200942231612678624742461898122651152"
    var_1 = module_0.func(*var_0)
    assert var_1 == "2"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xc8^\xdf\x10~N\x06\xf7\x04\xf6\xbdQ\xe23\x98"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "200942231612678624742461898122651152"
    list_1 = [var_0, var_0, var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "199999999999999999999999999999999999"
#    module_0.func()
