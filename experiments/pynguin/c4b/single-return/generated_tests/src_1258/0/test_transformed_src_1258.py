# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1258 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    list_0 = []
    bool_0 = False
    list_1 = [list_0, list_0, bool_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "7\\V`O(Ke13PUV704E"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "7\\V`O(Ke13PU7704E"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func()
