# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_921 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ":\\mx&go)?(W5^,l]DZ"
    tuple_0 = (str_0, str_0)
    dict_0 = {}
    list_0 = [tuple_0, dict_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
