# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2451 as module_0
import builtins as module_1


def test_case_0():
    complex_0 = -568.6 - 3971.2503j
    list_0 = [complex_0, complex_0, complex_0, complex_0]
    list_1 = [list_0, complex_0, list_0]
    var_0 = module_0.func(*list_1)


def test_case_1():
    bool_0 = True
    set_0 = {bool_0}
    list_0 = [set_0, bool_0, set_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bytes_0 = b"\x99\xdc\x8c\x16DSy|\x96\x8e~\xfdh\xb9\x8b"
    list_0 = []
    tuple_0 = (bool_0, bytes_0, list_0)
    list_1 = [tuple_0, tuple_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 361
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    list_1 = [list_0, int_0, int_0]
    var_0 = module_0.func(*list_1)
    str_0 = "('3BiiperqKD%oH&"
    list_2 = [str_0, str_0, str_0, str_0]
    module_1.object(*list_2, **var_0)
