# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0


def test_case_0():
    bytes_0 = b"\x04\xa0\n\xce\xbdB"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    list_1 = [bool_0, list_0]
    list_2 = [list_0, list_1, bool_0]
    var_0 = module_0.func(*list_2)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "0,73;Rhj"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -3016
    list_0 = [int_0, int_0]
    list_1 = [list_0, list_0, list_0, int_0]
    module_0.func(*list_1)
