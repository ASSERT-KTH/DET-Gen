# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_596 as module_0


def test_case_0():
    bytes_0 = b'\x9f\xeco\xa1\x9f^1(q\x98:\xe2\x1d\x8c\x1e"+!'
    var_0 = module_0.func(*bytes_0)


def test_case_1():
    bytes_0 = b'\x9fo\xa12\xb1\xef\x9f^\x1f(\x98:\xe2\x1d\x8c\x1e"+!'
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x07\x98\xd0\xac\x82i\x1c\x0b\x03\x1e\xb7\xd1\x98\xca?"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


def test_case_3():
    float_0 = 2015.0
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xfb\xc7\n(*\xc9;\x08\x02\xe8\xd1\x8a\x8a"
    var_1 = module_0.func(*bytes_0)