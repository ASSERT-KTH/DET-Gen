# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1541 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xaf/\x01\xd2\xd4tGF"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 212
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"E\xe8\xc3\x87\x96\x9aK\xb1\x91\xa0d"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
#    module_1.object(**var_0)
