# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1299 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b""
    bool_0 = False
    list_0 = [bool_0, bytes_0, bool_0, bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7


def test_case_2():
    bytes_0 = b"1"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"1"
    bool_0 = False
    list_0 = [bool_0, bytes_0, bool_0, bool_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 7
    list_1 = [var_0, bytes_0, bool_0, bool_0]
#    module_0.func(*list_1)
