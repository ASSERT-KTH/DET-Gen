# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_527 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xbf\x87\xac/&\xe0\x1e7\xdeR2!\xb1.\xd2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xbf\x87\xac/O\xe0\x1e\xdeR2!\xb1.\xd2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x13\x99\xac\xdd\xdd\xd2\x0f\x17"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 14
#    module_1.object(*var_0)
