# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_433 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "7{*ska:kb="
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "9).*s\x0bBa\nkbd"
    object_0 = module_1.object()
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    module_0.func(*var_0)
