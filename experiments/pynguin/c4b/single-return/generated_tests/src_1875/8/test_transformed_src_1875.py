# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1875 as module_0


def test_case_0():
    int_0 = 254
    list_0 = [int_0, int_0]
    list_1 = [list_0, list_0, int_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 508


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "jA*dGHA@|^d(M3U"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "|"
#    module_0.func()
