# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2670 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ".:C.I\\nl>wx"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "11"
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*var_1)
    assert var_2 == "1"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.func(*list_0)
