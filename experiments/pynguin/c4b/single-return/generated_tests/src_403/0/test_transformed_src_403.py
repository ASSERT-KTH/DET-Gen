# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_403 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x9f\xcbJ6!\r\x9d;\xdb\x1b\xf0\xb08\xfeP\n\xf5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xaf'\x7f2974\xde\xc0\xfe\xfd4\xbbh"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x9f\xcbJ6[!\r\x9d;\xdb\x1b\xf0\xb08\xfeP\n\xf5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_1.object(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"7\xa3@k\x90\xd9\xdb\x0c"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    var_1 = module_1.object()
#    module_0.func()
