# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_570 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -34
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "6"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)
