# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2613 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    int_0 = -939
    tuple_0 = (int_0, bool_0, int_0)
    list_0 = [tuple_0, bool_0, bool_0, bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    int_0 = -2106
    tuple_1 = (tuple_0, int_0, int_0)
    var_0 = module_0.func(*tuple_1)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "/fY<;Z}{%+jm8j@u2BV"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    var_2 = module_0.func(*list_0)
    assert var_2 == 0
#    module_0.func(*var_1)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "n?Y*2}c40kk&KhCbp"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    list_1 = []
#    module_0.func(*list_1)
