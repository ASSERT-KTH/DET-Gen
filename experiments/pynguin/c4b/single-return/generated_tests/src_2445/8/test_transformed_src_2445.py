# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2445 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Y\x0cD*EH4"
#    module_0.func(*str_0)


def test_case_2():
    str_0 = 'o\x0bT"s\t; Gv7YMykI\t'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "B\nB"
    list_0 = [str_0, str_0]
#    module_0.func(*list_0)
