# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import kheapsort as module_1


def test_case_0():
    object_0 = module_0.object()
    var_0 = module_1.kheapsort(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_1.kheapsort(list_0, bool_0)
    var_1 = module_1.kheapsort(bool_0, list_0)
    var_2 = module_1.kheapsort(var_1, bool_0)
    var_3 = module_1.kheapsort(var_0, bool_0)
    var_4 = module_1.kheapsort(var_1, var_1)
    var_5 = module_1.kheapsort(var_0, list_0)
    var_6 = module_1.kheapsort(var_4, var_4)
    var_7 = module_1.kheapsort(var_2, var_6)
    var_8 = module_1.kheapsort(var_7, var_6)
    module_0.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    bool_1 = False
    var_0 = module_1.kheapsort(list_0, bool_1)
    var_1 = module_1.kheapsort(list_0, list_0)
    var_2 = module_1.kheapsort(list_0, bool_0)
    var_3 = module_1.kheapsort(bool_0, bool_1)
    var_4 = module_1.kheapsort(var_2, bool_0)
    bool_2 = False
    var_5 = module_1.kheapsort(var_2, var_0)
    var_6 = module_1.kheapsort(bool_2, bool_2)
    var_7 = module_1.kheapsort(var_2, list_0)
    var_8 = module_1.kheapsort(var_6, bool_2)
    var_9 = module_1.kheapsort(var_2, var_6)
    var_10 = module_1.kheapsort(var_9, var_6)
    bool_3 = True
    var_11 = module_1.kheapsort(bool_3, var_0)
    var_12 = module_1.kheapsort(list_0, var_2)
    var_13 = module_1.kheapsort(var_8, var_10)
    var_14 = module_1.kheapsort(var_4, var_10)
    module_0.object(*var_2)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    bool_1 = True
    var_0 = module_1.kheapsort(list_0, bool_1)
    var_1 = module_1.kheapsort(list_0, bool_0)
    var_2 = module_1.kheapsort(list_0, var_1)
    var_3 = module_1.kheapsort(bool_1, var_2)
    none_type_0 = None
    var_4 = module_1.kheapsort(none_type_0, list_0)
    bool_2 = False
    var_5 = module_1.kheapsort(list_0, none_type_0)
    var_6 = module_1.kheapsort(bool_2, var_5)
    var_7 = module_1.kheapsort(var_1, none_type_0)
    dict_0 = {}
    var_8 = module_1.kheapsort(dict_0, var_1)
    complex_0 = 231.4028 - 2497.994j
    var_9 = module_1.kheapsort(complex_0, var_1)
    var_10 = module_1.kheapsort(bool_2, list_0)
    var_11 = module_1.kheapsort(var_6, var_4)
    var_12 = module_1.kheapsort(var_8, var_4)
    module_0.object(*var_5)