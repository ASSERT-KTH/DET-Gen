# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_478 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    list_0 = [set_0, set_0, set_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "huefJRkd87XC+0"
    module_0.func(*str_0)


def test_case_2():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "huefJRkd87XC+0"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    var_0 = module_1.object()
    str_0 = "\\4gq?(3X;XiKm9p"
    var_1 = module_0.func(*str_0)
    module_0.func()
