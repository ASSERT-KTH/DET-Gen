# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1534 as module_0


def test_case_0():
    str_0 = 'h?-b4^`+"=6`'
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = 'h?-b4^`+"=6`'
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "h?b4<e`+ll={o"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"
#    module_0.func()
