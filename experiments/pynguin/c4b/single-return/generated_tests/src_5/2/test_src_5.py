# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_5 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "2!Z-4-\x0c4@o6|"
    var_0 = module_0.func(*str_0)
    assert var_0 == 4
    module_0.func()
