# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    list_0 = []
    var_0 = module_0.kheapsort(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.kheapsort(list_0, bool_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.kheapsort(list_0, bool_0)
    var_1 = module_0.kheapsort(bool_0, bool_0)
    var_2 = module_0.kheapsort(bool_0, bool_0)
    var_3 = module_0.kheapsort(list_0, list_0)
    var_4 = module_0.kheapsort(var_1, var_3)
    var_5 = module_0.kheapsort(var_1, var_2)
    var_6 = module_0.kheapsort(var_2, var_2)
    set_0 = {bool_0, bool_0, bool_0}
    var_7 = module_0.kheapsort(var_2, var_2)
    none_type_0 = None
    var_8 = module_0.kheapsort(set_0, var_7)
    var_9 = module_0.kheapsort(bool_0, none_type_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    none_type_0 = None
    var_0 = module_0.kheapsort(list_0, none_type_0)
    module_1.object(*var_0)