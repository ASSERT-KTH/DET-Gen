# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1928 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 126.22
    str_0 = "X.D|:vh6"
    tuple_0 = (float_0, str_0)
    list_0 = [tuple_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    list_0 = [set_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "IGNORE HIM!"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
