# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "6p"
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


def test_case_1():
    bytes_0 = b""
    var_0 = module_0.flatten(bytes_0)


def test_case_2():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.flatten(list_1)
    object_0 = module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)
    none_type_1 = None
    var_1 = module_0.flatten(none_type_1)
    var_2 = module_0.flatten(var_1)
    var_3 = module_0.flatten(var_2)
    list_0 = [none_type_1, var_2]
    var_4 = module_0.flatten(none_type_1)
    list_1 = [var_1, list_0, list_0, var_1]
    var_5 = module_0.flatten(list_1)
    str_0 = "XuGa[^TWG\t"
    var_6 = module_0.flatten(list_1)
    var_7 = module_0.flatten(var_6)
    var_8 = module_0.flatten(var_5)
    var_9 = module_0.flatten(var_6)
    var_10 = module_0.flatten(var_8)
    var_11 = module_0.flatten(var_0)
    var_12 = module_0.flatten(str_0)
    var_13 = module_0.flatten(var_12)
    var_14 = module_0.flatten(var_8)
    var_15 = module_0.flatten(var_10)
    var_16 = module_0.flatten(var_5)
    var_17 = module_0.flatten(none_type_1)
    var_18 = module_0.flatten(var_6)
    module_1.object(*var_15)