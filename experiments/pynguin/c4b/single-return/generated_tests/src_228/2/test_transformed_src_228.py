# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_228 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1220
    set_0 = {int_0, int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "Howard"
    bool_0 = False
    list_0 = [bool_0]
    list_1 = [list_0, bool_0, bool_0, bool_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    bool_1 = False
    list_0 = [bool_0, bool_1, bool_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    list_1 = [var_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()