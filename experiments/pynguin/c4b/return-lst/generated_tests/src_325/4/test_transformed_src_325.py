# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_325 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    int_0 = -316
    bytes_0 = b"40\xaei\xa7\xe6Y\r}&\xc1KeW\xc7p{\xe2\x93\xe3"
    list_0 = [int_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -357
    bytes_0 = b"\\\x17X\xbc\x8d\xf9\xda4M\xb9\xd7\xd7t"
    list_0 = [int_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()