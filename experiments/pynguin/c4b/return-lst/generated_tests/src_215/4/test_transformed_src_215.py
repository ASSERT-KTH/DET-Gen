# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_215 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xd0\xaaL\x98\x02\x1e\xa2\\\xa0\xa2\xeb\x08\x84q\x07p\x88\x16o\x1a"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xff\x878\x99\x9f\xd8\x9f&+o\x07X\x88\x14\xf1"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"z\xd1\xda\x87\xff"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xe6\xa5b\xe2\x00KP\t\x0f%5F"
    var_0 = module_0.func(*bytes_0)
    bytes_1 = b"&\rQ\x85h\xfe|\xc8\xab%\xda\xd6\n'v"
    var_1 = module_0.func(*bytes_1)
#    module_1.object(**var_1)
