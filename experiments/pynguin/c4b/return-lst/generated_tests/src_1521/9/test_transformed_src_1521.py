# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1521 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"z\xcf\xfc\x81\xb3'"
    int_0 = 2
    list_0 = [int_0, bytes_0, bytes_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    bytes_0 = b"8\xdf\x9b\x9bY\xe2\xd1D|H!u\x036\xe3d\xd0@"
    int_0 = 5
    list_0 = [int_0, bytes_0, int_0]
    var_0 = module_0.func(*list_0)