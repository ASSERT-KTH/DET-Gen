# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1580 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "3+Jff [Y1`>A8qn*vQ"
    var_0 = module_0.func(*str_0)
    assert var_0 == "7"
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "7"
#    module_1.object(**var_1)
