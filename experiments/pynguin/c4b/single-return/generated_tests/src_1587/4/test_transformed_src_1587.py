# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1587 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xb0\xa1\x91\x13\xd2\x06\xd5\xf4"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
#    module_0.func()
