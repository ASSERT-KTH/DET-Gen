# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1008 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    bytes_0 = b"\xfc\xb9\x88g,\x05\x99\xd5\x94z\xd5\xe6\xae\x14\x91"
    int_0 = 2219
    tuple_0 = (list_0, bytes_0, int_0)
    var_0 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "P7HB"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1608
    list_0 = [int_0]
    tuple_0 = (list_0,)
    list_1 = [list_0, list_0, int_0, tuple_0]
    var_0 = module_0.func(*list_1)
    module_0.func()
