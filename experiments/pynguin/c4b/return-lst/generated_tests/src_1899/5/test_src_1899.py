# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1899 as module_0
import builtins as module_1


def test_case_0():
    int_0 = 407
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xde1d>O\xeb\xb2Qy"
    var_0 = module_0.func(*bytes_0)
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    set_0 = {bool_0}
    var_0 = module_0.func(*set_0)
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x02d>O\xf6\xbf\xeb\xb2Qy"
    var_0 = module_0.func(*bytes_0)
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    module_0.func(*list_0)