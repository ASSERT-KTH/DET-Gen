# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1942 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"h\xd7\x87\xd2J\xd8D\x8aO"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc3\x14d\xc1\x9b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x14d\xc1\x9b\xf9\x8f"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 14
#    module_0.func()
