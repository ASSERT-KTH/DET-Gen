# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1477 as module_0


def test_case_0():
    str_0 = "7"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"\x1f[\x1e66#.c@\x81<5\x8a\xfd\x03\xed\x1e\x04"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "7"
    list_0 = [str_0, str_0, str_0, str_0]
    list_1 = [list_0, list_0, str_0]
    var_0 = module_0.func(*list_1)
    list_2 = [var_0, str_0]
    var_1 = module_0.func(*list_2)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "7"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [list_0, list_0, str_0]
    var_0 = module_0.func(*list_1)
    module_0.func()
