# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2222 as module_0


def test_case_0():
    str_0 = "_;IA 6O"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "H/sZWhjT 8.!+W_>cBg"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"


def test_case_3():
    str_0 = "Xb&TQ2A8k]NM\\\rJh"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


def test_case_4():
    str_0 = "9"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
