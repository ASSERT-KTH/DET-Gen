# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_845 as module_0
import builtins as module_1


def test_case_0():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    list_1 = [list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "aR*NB3"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "aRQNB3"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_1.object(*var_0)
