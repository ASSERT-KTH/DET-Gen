# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2026 as module_0


def test_case_0():
    int_0 = 4
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Rajesh"
    var_1 = module_0.func(*list_0)
    assert var_1 == "Rajesh"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 16
    tuple_0 = (int_0,)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "Sheldon"
#    module_0.func()
