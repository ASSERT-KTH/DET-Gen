# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_895 as module_0


def test_case_0():
    str_0 = " 7&bJ_]8C:\t7T="
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "Plc4v9^KV2O(2$mTnA+"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "Plc4vH^KV2O(2$mTnA+"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "W[\nQf\\0<^6Z"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    tuple_0 = (var_1, var_1, var_0)
    var_2 = module_0.func(*tuple_0)
