# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1163 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "m9s@Ao2"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
