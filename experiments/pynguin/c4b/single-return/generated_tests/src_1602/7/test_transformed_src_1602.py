# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1602 as module_0


def test_case_0():
    str_0 = "tA0 EoA"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
