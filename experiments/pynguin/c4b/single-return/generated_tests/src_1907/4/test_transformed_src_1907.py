# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1907 as module_0


def test_case_0():
    str_0 = "W\r\t]"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "$\ryr<ET BBj"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "$\ryr<ET B-WWj"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()
