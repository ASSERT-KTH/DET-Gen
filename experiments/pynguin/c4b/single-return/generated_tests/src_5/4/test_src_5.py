# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_5 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "2t[po.@N{Ar*m:1vv!"
    var_0 = module_0.func(*str_0)
    assert var_0 == 4
    module_0.func()
