# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1539 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "kbqa"
    var_0 = module_0.func(*str_0)
    assert var_0 == "K"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ";"
    list_0 = [str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == ";"
    var_1 = module_0.func(*list_0)
    list_1 = [list_0, list_0, str_0]
    var_2 = module_0.func(*list_1)
    module_0.func()


def test_case_3():
    str_0 = "kbqa"
    var_0 = module_0.func(*str_0)
    assert var_0 == "K"
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    assert var_1 == "k"


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "2Y2{6Zpeg~yC%"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "2Y2{6Zpeg~yC%"
    module_0.func()
