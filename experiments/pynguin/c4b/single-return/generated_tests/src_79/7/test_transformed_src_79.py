# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_79 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 502
    bytes_0 = b"l\xd9\xce"
    list_0 = [int_0, bytes_0, bytes_0, int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 528
    bytes_0 = b""
    list_0 = [int_0, bytes_0, bytes_0, int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1902
    bytes_0 = b""
    list_0 = [int_0, bytes_0, bytes_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "chest"
#    module_0.func(*var_0)
