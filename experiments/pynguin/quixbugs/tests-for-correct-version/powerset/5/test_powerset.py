# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import powerset as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.powerset(object_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_1.powerset(none_type_0)


def test_case_2():
    none_type_0 = None
    var_0 = module_1.powerset(none_type_0)
    dict_0 = {}
    var_1 = module_1.powerset(dict_0)
    var_2 = module_1.powerset(var_1)
    var_3 = module_1.powerset(dict_0)
