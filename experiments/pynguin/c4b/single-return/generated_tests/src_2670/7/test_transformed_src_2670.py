# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2670 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = 'aoS["'
    bool_0 = False
    list_0 = [bool_0, str_0, bool_0, bool_0]
    dict_0 = module_0.func(*list_0)
    assert dict_0 == "5"
    list_1 = [str_0, dict_0, bool_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()
