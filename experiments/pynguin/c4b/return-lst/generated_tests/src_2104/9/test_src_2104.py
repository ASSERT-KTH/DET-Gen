# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2104 as module_0


def test_case_0():
    str_0 = "cc;c=Hpm"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe8N\xabB\xde\xd1\xe9\xd9"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
    int_0 = -698
    list_0 = [dict_0, bytes_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "QI>x5bo"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ".1fvTrNie9?8&"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    bool_0 = False
    module_0.func(*bool_0)
