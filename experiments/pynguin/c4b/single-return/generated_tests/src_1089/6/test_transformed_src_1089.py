# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1089 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    int_0 = 923
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES\n0"


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa6\xa5\xbd\x92t\xbf\xb0\x8c\x8c}2\xea"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "NO"
#    module_0.func()
