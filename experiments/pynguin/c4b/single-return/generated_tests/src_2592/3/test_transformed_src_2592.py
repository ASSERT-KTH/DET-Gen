# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1695
    str_0 = "UmO#'*X"
    bytes_0 = b"\xd1\x7fY,\xeb\xdf9\x1eA'\xb4x\xa4\xaf\xc5\xe6{"
    tuple_0 = (int_0, int_0, str_0, bytes_0)
    bool_0 = False
    bool_1 = True
    tuple_1 = (int_0, tuple_0, bool_0, bool_1)
    list_0 = [tuple_1, str_0, tuple_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    tuple_0 = (bool_0,)
    list_0 = [tuple_0, tuple_0, tuple_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "v@"
    list_0 = [str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "999999"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 999999
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "9959.9"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 989999
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "9999W9"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 999899
#    module_0.func()