# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.kheapsort(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ",tC et"
    var_0 = module_0.kheapsort(str_0, str_0)
    none_type_0 = None
    var_1 = module_0.kheapsort(none_type_0, str_0)
    var_2 = module_0.kheapsort(str_0, str_0)
    list_0 = [str_0, str_0, str_0]
    int_0 = -2071
    var_3 = module_0.kheapsort(list_0, int_0)
    var_4 = module_0.kheapsort(var_3, str_0)
    bool_0 = True
    var_5 = module_0.kheapsort(var_2, bool_0)
    object_0 = module_1.object()
    var_6 = module_0.kheapsort(var_4, var_3)
    var_7 = module_0.kheapsort(var_4, object_0)
    module_1.object(*var_3)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ""
    none_type_0 = None
    var_0 = module_0.kheapsort(none_type_0, str_0)
    var_1 = module_0.kheapsort(none_type_0, str_0)
    var_2 = module_0.kheapsort(str_0, str_0)
    list_0 = [str_0, str_0, str_0]
    int_0 = 3322
    var_3 = module_0.kheapsort(list_0, int_0)
    var_4 = module_0.kheapsort(var_3, str_0)
    object_0 = module_1.object()
    var_5 = module_0.kheapsort(var_4, var_3)
    var_6 = module_0.kheapsort(var_4, object_0)
    list_1 = [int_0]
    var_7 = module_0.kheapsort(list_1, var_3)
    module_1.object(*var_3)