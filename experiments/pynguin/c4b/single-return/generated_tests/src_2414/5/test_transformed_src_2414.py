# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2414 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "7"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Sheldon"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Howard"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "98"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Leonard"
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "Leonard"
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
#    module_1.object(**dict_0)
