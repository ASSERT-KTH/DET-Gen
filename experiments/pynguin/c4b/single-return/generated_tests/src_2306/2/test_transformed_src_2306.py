# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2306 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xbf\x8d\xb9\xa8,\x98N\xe3\xc0,\x1dL"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xbf\x8d\xb9,\xe9\xcb\xe3\xc0L"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 8
#    module_1.object(**var_0)