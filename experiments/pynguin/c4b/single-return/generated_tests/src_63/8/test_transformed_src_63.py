# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_63 as module_0


def test_case_0():
    int_0 = 255
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
