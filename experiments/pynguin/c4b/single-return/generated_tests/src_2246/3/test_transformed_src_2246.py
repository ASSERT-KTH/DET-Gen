# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2246 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "L!|7Ifo%OZR$H"
    bool_0 = True
    int_0 = 43
    tuple_0 = (str_0, bool_0, int_0)
    list_0 = [tuple_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "IGNORE HIM!"
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
    dict_1 = {}
    list_1 = [dict_1, dict_1]
    var_1 = module_0.func(*list_1)
    assert var_1 == "CHAT WITH HER!"
#    module_0.func()
