# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kheapsort as module_0
import builtins as module_1


def test_case_0():
    str_0 = "JX\\\x0cS 0%G_ *+"
    var_0 = module_0.kheapsort(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 323
    list_0 = [int_0]
    var_0 = module_0.kheapsort(list_0, list_0)
    var_1 = module_0.kheapsort(list_0, int_0)
    module_1.object(*var_1)


def test_case_2():
    int_0 = 306
    list_0 = []
    var_0 = module_0.kheapsort(list_0, list_0)
    var_1 = module_0.kheapsort(int_0, var_0)
    var_2 = module_0.kheapsort(list_0, int_0)
    object_0 = module_1.object(*var_2)
    var_3 = module_0.kheapsort(var_2, object_0)
    var_4 = module_0.kheapsort(int_0, var_0)
    set_0 = set()
    var_5 = module_0.kheapsort(set_0, var_2)
    var_6 = module_0.kheapsort(var_2, var_0)
    var_7 = module_0.kheapsort(var_2, int_0)
    var_8 = module_0.kheapsort(var_0, var_5)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 323
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.kheapsort(list_0, int_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -1088
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.kheapsort(list_0, int_0)
    module_1.object(*var_0)