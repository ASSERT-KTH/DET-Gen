# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2158 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "]aq\\F1(P?]'+"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "10:01"


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "]aq\\F1(P?]'+"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "10:01"
    list_1 = [var_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "11:11"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "+3Q`ALk4Hs7"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "04:40"
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "16EG$_`VZl9_e`\r{;\tD"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "20:02"
    module_1.object(*var_0)
