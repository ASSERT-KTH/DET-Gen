# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1139 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bytes_0 = b"8\xfc\x96_\x95\xf3dHd\xb8"
    list_0 = [bool_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'"\xa5\x9e\xea\xf3e'
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x15\x0c\xc5\xcf\xa2"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x14\xe3\xf0\xaf\x07x\xee| \x8a\xeb\x96\xbb\xa9\xc7"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    module_0.func()
