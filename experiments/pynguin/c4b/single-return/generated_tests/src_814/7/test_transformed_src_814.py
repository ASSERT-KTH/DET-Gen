# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_814 as module_0
import builtins as module_1


def test_case_0():
    int_0 = -1043
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1045
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "444"
    object_0 = module_1.object()
#    module_0.func()


def test_case_3():
    int_0 = -1060
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "4"
    var_1 = module_0.func(*var_0)
    assert var_1 == "4"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 713.13281
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "44444777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777"
    )
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1"
    list_1 = [var_0, var_0, bool_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "-1"
    float_0 = 713.13281
    list_2 = [float_0, float_0, float_0, float_0]
    var_2 = module_0.func(*list_2)
    assert (
        var_2
        == "44444777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777"
    )
    var_3 = module_0.func(*var_2)
    assert var_3 == "4"
    var_4 = module_1.object()
    var_5 = module_1.object()
#    module_0.func()
