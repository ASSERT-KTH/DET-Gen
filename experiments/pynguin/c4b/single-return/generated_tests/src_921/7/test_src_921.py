# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_921 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ")mVK(P"
    str_1 = "e%3qTX"
    list_0 = [str_1, str_1, str_0, str_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == 6
    module_0.func()
