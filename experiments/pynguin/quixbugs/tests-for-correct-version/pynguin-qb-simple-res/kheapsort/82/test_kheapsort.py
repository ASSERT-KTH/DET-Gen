# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    str_0 = "c5]vlNE:\r7"
    var_0 = module_0.kheapsort(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    list_0 = []
    var_0 = module_0.kheapsort(list_0, none_type_0)
    object_0 = module_1.object(*var_0)
    var_1 = module_0.kheapsort(none_type_0, none_type_0)
    var_2 = module_0.kheapsort(var_0, var_0)
    int_0 = -773
    module_1.object(**int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    var_0 = module_0.kheapsort(none_type_0, none_type_0)
    list_0 = [none_type_0]
    var_1 = module_0.kheapsort(list_0, none_type_0)
    module_1.object(*var_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    list_0 = [tuple_0]
    var_0 = module_0.kheapsort(tuple_0, tuple_0)
    none_type_0 = None
    var_1 = module_0.kheapsort(var_0, var_0)
    var_2 = module_0.kheapsort(var_0, list_0)
    var_3 = module_0.kheapsort(list_0, none_type_0)
    module_1.object(*var_3)


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(none_type_0, none_type_0)
    var_1 = module_1.object()
    var_2 = module_0.kheapsort(list_0, none_type_0)
    var_3 = module_0.kheapsort(none_type_0, tuple_0)
    module_1.object(*var_2)