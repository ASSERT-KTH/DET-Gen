# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_249 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 480
    list_0 = [int_0, int_0]
    list_1 = [int_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "Penny"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
