# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_908 as module_0


def test_case_0():
    bytes_0 = b":@\x98\x99oG$\xff"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b":@\x99\x99oG$\xff"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    bytes_0 = b"\x99\x99\x99\x99\x99\x99\x995\x89\xfag\xdb\xf6Xd\xc8"
    list_0 = [
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
        bytes_0,
    ]
    var_0 = module_0.func(*list_0)
