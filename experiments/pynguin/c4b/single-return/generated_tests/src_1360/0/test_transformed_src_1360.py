# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1360 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    var_1 = module_0.func(*list_0)
    assert var_1 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1163
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 894.723626
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "444777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777"
    )
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0]
#    module_1.object(*list_1)
