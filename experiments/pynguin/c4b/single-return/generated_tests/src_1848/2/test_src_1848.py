# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1848 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"\xd3\x83O\xb3w\x81\x11\xfdc\x98\xd0\xbb\xa1\x90"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd3\x83OL\xb3w\x815\x11\xfdc\x98\xd0\xbb\xa1\x9e\x90"
    int_0 = -3318
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    module_0.func(*int_0)


def test_case_3():
    bytes_0 = b"\x1c\xa9\xcb1o \x0f\xb4\xf8$"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
