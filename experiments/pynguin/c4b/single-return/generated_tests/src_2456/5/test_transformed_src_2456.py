# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2456 as module_0


def test_case_0():
    float_0 = 681.98382
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 353


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
