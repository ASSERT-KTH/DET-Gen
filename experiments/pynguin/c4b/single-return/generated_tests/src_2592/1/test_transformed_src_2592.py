# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    list_1 = [list_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "45JROM9\\\n+mC0)"
    var_0 = module_0.func(*str_0)
    assert var_0 == 4
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "45JROM9\\\n+C0)"
    list_0 = [str_0, str_0, str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2476
    str_0 = 'x/&z\n\n"d'
    tuple_0 = (int_0, str_0)
    list_0 = [tuple_0, tuple_0, str_0, int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "s\n"
    list_0 = [str_0, str_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "99999999"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99999999
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "9999999G"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 99999989
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "s8"
    list_0 = [str_0, str_0]
#    module_0.func(*list_0)
