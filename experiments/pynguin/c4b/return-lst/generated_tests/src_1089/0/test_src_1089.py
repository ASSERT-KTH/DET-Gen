# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1089 as module_0


def test_case_0():
    bytes_0 = b"\x04\x0f@+\xcb\x07\xec\xcc;\xc7R*\x16\xe2\xd8{\xad/\xc2\xcb"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x04@+\xcb\x07\xec\x11\xcc;\xc7R*\x16\xe2{\xad/\xc2\xcb"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)