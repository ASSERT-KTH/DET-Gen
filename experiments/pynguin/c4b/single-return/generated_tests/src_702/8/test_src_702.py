# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_702 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x87\x83o\x9c\\\xc9\xf3\xfc\x7f\xdf\xe8\x94\x1761B"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"r\x12\xee\xb1b\x19^\x00\xfb["
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x12\xee\xb1b\x19^\x00["
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func(*var_0)
