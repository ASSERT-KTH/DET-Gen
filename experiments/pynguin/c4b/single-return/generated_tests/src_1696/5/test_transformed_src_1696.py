# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1696 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    int_0 = -1575
    list_0 = [int_0]
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == -1575
