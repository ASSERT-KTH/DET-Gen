# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1387 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b""
    list_0 = []
    list_1 = [list_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    module_0.func(*list_0)


def test_case_1():
    str_0 = "ib8Z#6{D5\x0bo"
    object_0 = module_1.object()
    list_0 = [str_0, object_0, object_0, object_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 2254.51
    module_0.func(*float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1606
    dict_0 = {int_0: int_0, int_0: int_0}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
    module_0.func()