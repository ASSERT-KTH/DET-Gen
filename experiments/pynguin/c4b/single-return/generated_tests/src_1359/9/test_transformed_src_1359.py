# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1359 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x81lj\x89\xfa\x87\xd1g\x11a\x92\x10\x95\x0fK\x85"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "hnMY!c+3v#|tEAR"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


def test_case_3():
    str_0 = "x8!"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "hnMY!c+@3v#|tEAR"
    tuple_0 = (str_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 5
    str_1 = "}1XmiR\x0c\\\t\n]$z\\&A2:."
    list_0 = [str_1, str_1, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 5
#    module_0.func(*var_0)


def test_case_5():
    str_0 = "ax8!"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "a8"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
#    module_1.object(**var_0)
