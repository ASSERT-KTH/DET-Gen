# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2294 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "BjfND\rYviU_Ab9z$-X"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "BjfND\rYviU_Ab9z$-X"
    dict_0 = {}
    list_0 = [str_0, str_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func()
