# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_401 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"1"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"1"
    list_0 = [bytes_0, bytes_0, bytes_0]
    bool_0 = False
    list_1 = [bool_0, bytes_0, bytes_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 7
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"1"
    float_0 = 2241.2959
    list_0 = [float_0, bytes_0, bytes_0]
#    module_0.func(*list_0)
