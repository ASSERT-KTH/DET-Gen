# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_735 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "\x0b9Nb"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\x0b9N"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\n05830068"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 830073
    var_1 = module_0.func(*str_0)
    assert var_1 == -1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\n58630068"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 863019
    var_1 = module_0.func(*list_0)
    assert var_1 == 863019
    module_0.func()


def test_case_5():
    str_0 = " 080"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "\n586237068"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 862443
    var_1 = module_0.func(*str_0)
    assert var_1 == -1
    module_1.object(**var_1)
