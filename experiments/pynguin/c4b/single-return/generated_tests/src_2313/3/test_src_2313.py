# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2313 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Swmif)yI"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".s"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Swmif)yI"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*str_0)
    assert var_0 == ".s"
    var_1 = module_0.func(*set_0)
    assert var_1 == ".s.w.m.f.)"
    module_1.object(*var_1, **set_0)
