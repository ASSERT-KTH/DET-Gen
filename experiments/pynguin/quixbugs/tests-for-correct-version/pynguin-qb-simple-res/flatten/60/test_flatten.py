# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "w8zdO 0I>'{"
    var_0 = module_0.flatten(str_0)
    module_1.object(*var_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)


def test_case_2():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.flatten(list_1)
    object_0 = module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)
    list_0 = [none_type_0]
    var_1 = module_0.flatten(list_0)
    list_1 = [list_0]
    var_2 = module_0.flatten(list_1)
    module_1.object(*var_2)