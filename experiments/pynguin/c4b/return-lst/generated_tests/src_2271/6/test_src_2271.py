# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2271 as module_0


def test_case_0():
    bytes_0 = b"b\x1d\xf5\x0c\x84\xe5\x00X\xa5\xbc "
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "E1\te]"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"b\x1d\xf5\x0c\x84\xe5\x00X\xa5\xbc "
    module_0.func(*bytes_0)


def test_case_3():
    str_0 = "=\n=\n\n=="
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
