# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1389 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "DzVTMjn03Uo&g9? -`[S"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "11"


def test_case_2():
    str_0 = "&xXO5LLMz0A\x0b1bo"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "zlIPZXd:2]x"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "9"
    object_0 = module_1.object()
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "&xXO5LLOYMz0A\x0b1bo"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "5"
    var_1 = module_0.func(*str_0)
    assert var_1 == "2"
#    module_1.object(*var_1)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "rlP!|Eb>jF3I 58PXK"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    var_1 = module_0.func(*list_0)
    assert var_1 == "7"
#    module_0.func()
