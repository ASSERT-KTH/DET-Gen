# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_769 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 754.608062
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 389
#    module_0.func()


def test_case_1():
    bool_0 = False
    bool_1 = True
    list_0 = [bool_0, bool_0, bool_1, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
