# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xba\xc1\xc9\x89L\xd1\xed\xef2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe62\xf3\xd1\xf3Z?P\x94C1\x9d"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xd9\x1a\xa1\xd0wo8V\x86L\xa5\x8d\x8e\xb5F\x8e*\x89\xba\xe1"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xd62\x0b\x84`JA\xb7\xf7}O\xb0\\\xd5\xd1\xfc"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 9
#    module_0.func()