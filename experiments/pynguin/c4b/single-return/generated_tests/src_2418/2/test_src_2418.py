# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2418 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "(4NO{"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "(4no{"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "=JE6"
    var_0 = module_0.func(*str_0)
    assert var_0 == "="
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\\'#t,Ze<GOBMZs29K"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\\'#t,Ze<GOBMZs29K"
    var_1 = module_0.func(*str_0)
    assert var_1 == "\\"
    module_1.object(*var_1)
