# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2015 as module_0


def test_case_0():
    int_0 = 3767
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"j\xe3\xd0\x82\x0b\x1c\x15"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x13\xefQvdP\xbb\xf88`\xe7V"
    var_0 = module_0.func(*bytes_0)
    module_0.func()