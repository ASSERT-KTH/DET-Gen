# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1307 as module_0


def test_case_0():
    str_0 = "KdI"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    int_0 = 2949
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "7"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"]Y\x0b\x19.\x8b2\xb8\xcaK\xdc\xe5FV\xa1\x84"
    list_0 = [bytes_0]
    int_0 = -1979
    tuple_0 = (list_0, int_0)
    str_0 = "F"
    tuple_1 = (tuple_0, str_0)
    list_1 = [tuple_1, list_0, tuple_0, tuple_0]
    list_2 = [list_1]
    bool_0 = True
    tuple_2 = (list_2, bool_0, int_0, bool_0)
    var_0 = module_0.func(*tuple_2)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"C\xb3:\x0c\xc6\x16v\xd4)\x80\x16\xa4>\x97\xb2\xb7"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
