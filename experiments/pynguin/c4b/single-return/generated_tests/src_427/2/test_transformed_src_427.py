# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_427 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ")FHXXUoZi_8D;MrQ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 11
    list_1 = [str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 11
#    module_0.func(*var_1)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
