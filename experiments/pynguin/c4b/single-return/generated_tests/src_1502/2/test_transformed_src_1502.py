# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1502 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "0 0"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -267.64445037424525
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-75 -74"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -272.114
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-76 -75"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -1208.3406
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "-344 -342"
#    module_1.object(**var_0)