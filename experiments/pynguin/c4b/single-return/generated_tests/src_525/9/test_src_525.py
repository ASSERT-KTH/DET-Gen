# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_525 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "_"
    var_0 = module_0.func(*str_0)
    assert var_0 == "._"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "$x*iA),e'$lkF"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".$.x.*.).,.'.$.l.k.f"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "o"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "U;"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".;"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "nYVm7k"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".n.v.m.7.k"
    module_0.func()
