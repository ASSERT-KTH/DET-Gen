# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2230 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "U=,/S(;.Egtt\x0bN;;O}#^"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "9\\1[U\\,*7oGSAu"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*var_0)
    assert var_1 == "NO"
