# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1541 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"@<\xf6\xc8*V\x8c\xc9\x0c\xbcD\x04\xbd\x94\x8b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0


def test_case_2():
    bytes_0 = b"@<\xc8\xbfV\x8c\xc9\x0c\xbcD\x1c\x04\xbd\x94\x8b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"]\xbb\x13\t\xda\xce\x93\xab\x04o"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 37
#    module_0.func()
