# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2170 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2750
    bool_0 = False
    dict_0 = {int_0: int_0, int_0: int_0}
    list_0 = [bool_0, dict_0, int_0]
    list_1 = [int_0, int_0, bool_0, list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func(*int_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()