# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"Z"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"a\xa1\xd2l^"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    list_0 = [var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 3
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x17\xa3\x10\x0f\xbdFS\xd5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xa1l"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"U@\x84\x91\x06\x1a\x12\\TG\xd0F\xca\x90ny\x14P\xf4L"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    list_0 = [var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
#    module_1.object(*list_0)
