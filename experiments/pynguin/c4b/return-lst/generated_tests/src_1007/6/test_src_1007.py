# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1007 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "3xd4)#-.@GZ"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "4"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0aE$*PA[c!$:A|B:Vy"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = '1F"~N'
    var_0 = module_0.func(*str_0)
    module_1.object(*var_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "5{"
    var_0 = module_0.func(*str_0)
    module_1.object(*str_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = '2y^VHDn[CO"'
    var_0 = module_0.func(*str_0)
    module_0.func()
