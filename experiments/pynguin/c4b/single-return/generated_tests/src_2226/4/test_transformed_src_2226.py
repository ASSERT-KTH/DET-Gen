# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xfc\xe2\x90\xb9\xadH\xfe\xa7\xd8\x96\xd2\x86\xf6f\x94{\x98"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xfc\xe2\x10)\xadG\xfe\xd8\x96\x86\xf6f\x94{"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 14
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'\xce"\xdc9\xef\xf71\xf0\x19\xd4'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 13
    var_1 = module_1.object()
#    module_0.func()
