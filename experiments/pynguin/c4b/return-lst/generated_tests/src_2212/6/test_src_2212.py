# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2212 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1318
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"9\xd5\x1b\xd6\xa7\xf3\x0b{\xf3\x02Uj\xf8\x1d\x97f-\x03\xee\xdb"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "37#+d:"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "23#+:"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)
    module_0.func()
