# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1169 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 3315.5094
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 6071549575
    module_0.func()
