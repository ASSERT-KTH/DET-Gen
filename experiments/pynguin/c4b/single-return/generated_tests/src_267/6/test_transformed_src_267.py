# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_267 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 35.5
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Howard"
    list_1 = [float_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "Howard"
#    module_0.func(*float_0)
