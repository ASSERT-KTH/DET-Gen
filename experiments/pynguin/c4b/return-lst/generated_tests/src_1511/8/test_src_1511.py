# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1511 as module_0


def test_case_0():
    bytes_0 = b"\x8c\xe5\x8d\xe8\xcar\x95\r%\xc1\xf0\xd3\x92!v\x14:"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    float_0 = 176.8
    tuple_0 = (float_0, float_0)
    dict_0 = {tuple_0: float_0}
    list_0 = [dict_0, float_0, dict_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "h5d1]]Tsu"
    var_0 = module_0.func(*str_0)
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "h5d1]]Tsu"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    none_type_0 = None
    module_0.func(*none_type_0)


def test_case_5():
    bytes_0 = b"D"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
