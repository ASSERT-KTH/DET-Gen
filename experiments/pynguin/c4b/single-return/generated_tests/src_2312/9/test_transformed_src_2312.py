# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2312 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "jH"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".j.h"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "by"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".b"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".b"
#    module_0.func()
