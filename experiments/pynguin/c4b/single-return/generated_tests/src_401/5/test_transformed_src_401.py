# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_401 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = False
    bytes_0 = b""
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    bytes_0 = b""
    list_0 = [bool_0, bytes_0]
#    module_0.func(*list_0)


def test_case_3():
    bool_0 = True
    bytes_0 = b"6"
    list_0 = [bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"6"
    float_0 = 569.56
    list_0 = [float_0, bytes_0, bytes_0]
#    module_0.func(*list_0)