# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2110 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "qb_\n>e"
    list_0 = [str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "4c|\x0b[o5DIj(#G\x0cZ$9,"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "qb\n"
    var_0 = module_0.func(*str_0)
    module_1.object(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "r,?"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    int_0 = 1650
    module_0.func(*int_0)
