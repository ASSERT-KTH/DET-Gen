# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_545 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "hw)$*l]r^>nsc.HvT"
    bool_0 = True
    list_0 = [bool_0, str_0, bool_0, str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -16
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "y"
    bool_0 = False
    list_0 = [bool_0, str_0, bool_0, str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    module_0.func()
