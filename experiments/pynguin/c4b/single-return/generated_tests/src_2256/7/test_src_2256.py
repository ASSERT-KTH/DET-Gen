# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2256 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "eO9d|`Pcm0\\@`"
    list_0 = [str_0, str_0, str_0, str_0]
    dict_0 = {}
    int_0 = 1284
    tuple_0 = (list_0, dict_0, int_0)
    list_1 = [tuple_0, tuple_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 3375
    str_0 = "|d/M&"
    list_0 = [str_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".d.m"
    module_0.func()
