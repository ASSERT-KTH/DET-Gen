# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1469 as module_0


def test_case_0():
    bytes_0 = b"\x83\x02\xec\xe9\x98E\xd3\xc4\x9c\n"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x85\x12\x17\xe8\xd0\x82\xcc\xb4\xa3\x86/\xbb"
    var_0 = module_0.func(*bytes_0)
    list_0 = [var_0, var_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
