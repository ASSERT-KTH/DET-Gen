# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_490 as module_0


def test_case_0():
    str_0 = "^Q#\t.kR_h*0el;Y\rT3"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "q#\t.kn7R?vh*}el;l\roT"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [str_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
