# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1705 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'O\xe2\x04\x07\xf5R_\x93\xcfZ"\x01'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x8f\xde\x005\x97\xda\xe8o}$z\xc3\xf3\xbb\x08\xe2\x043"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 143
#    module_0.func(*var_0)