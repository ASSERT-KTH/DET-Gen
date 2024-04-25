# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    float_0 = -2290.5645
    var_0 = module_0.kheapsort(float_0, float_0)


def test_case_1():
    list_0 = []
    bool_0 = False
    var_0 = module_0.kheapsort(list_0, bool_0)
    object_0 = module_1.object()
    none_type_0 = None
    var_1 = module_0.kheapsort(object_0, none_type_0)
    var_2 = module_0.kheapsort(var_1, var_1)
    bool_1 = False
    list_1 = [bool_1, bool_1, bool_1, bool_1]
    list_2 = [list_1, list_1]
    var_3 = module_0.kheapsort(var_2, var_2)
    var_4 = module_0.kheapsort(list_2, bool_1)
    bytes_0 = b"\xdf&&"
    var_5 = module_0.kheapsort(bytes_0, list_1)
    object_1 = module_1.object(*var_0)
    var_6 = module_0.kheapsort(list_1, bool_1)
    var_7 = module_0.kheapsort(list_2, var_6)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0, list_0]
    bool_1 = False
    var_0 = module_0.kheapsort(bool_0, bool_1)
    var_1 = module_0.kheapsort(list_0, bool_0)
    var_2 = module_0.kheapsort(list_1, bool_0)
    module_1.object(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "=M("
    var_0 = module_0.kheapsort(bool_0, str_0)
    none_type_0 = None
    object_0 = module_1.object()
    none_type_1 = None
    bool_1 = True
    var_1 = module_0.kheapsort(var_0, var_0)
    list_0 = [bool_1, bool_1, bool_1, bool_1]
    bool_2 = False
    var_2 = module_0.kheapsort(bool_0, var_0)
    var_3 = module_0.kheapsort(list_0, none_type_0)
    var_4 = module_0.kheapsort(bool_2, bool_0)
    var_5 = module_0.kheapsort(var_1, none_type_1)
    object_1 = module_1.object()
    module_1.object(*var_3)