# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1948 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -2783
    list_0 = [int_0, int_0, int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2766
    list_0 = [int_0, int_0, int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"9\xe2W\x9c\x87\x03\xaf2"
    module_0.func(*bytes_0)
