# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1359 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "b53 "
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x91Z"
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "a*0(x-=O<t\nO'|"
    list_0 = [str_0, str_0]
    object_0 = module_0.func(*list_0)
    assert object_0 == 5
#    module_0.func()


def test_case_3():
    str_0 = "}1\rjtYPrh'"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


def test_case_4():
    str_0 = "h`lQ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "t8XMq~L\tde"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "h8Ir"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
#    module_1.object(*var_0, **var_0)
