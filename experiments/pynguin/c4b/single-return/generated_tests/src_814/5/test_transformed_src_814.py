# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_814 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1381
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "444"
#    module_0.func()


def test_case_3():
    float_0 = -2123.596
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "444"
    list_1 = [var_0, float_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "444444777777777777777777777777777777777777777777777777777777777777"
    var_2 = module_0.func(*var_0)
    assert var_2 == "4"
    var_3 = module_0.func(*var_1)
    assert var_3 == "4"


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    int_0 = -2120
    list_0 = [bool_0, bool_0, bool_0, int_0, bool_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-1"
    bytes_0 = b"L\xce\xf2\x94GD\\\x96\xa8,\xb8\x8a=("
    var_1 = module_0.func(*bytes_0)
    assert var_1 == "4444477777777"
    var_2 = module_0.func(*var_1)
    assert var_2 == "4"
    list_1 = [var_0, var_2]
    var_3 = module_0.func(*list_1)
    assert var_3 == "-1"
#    module_0.func()
