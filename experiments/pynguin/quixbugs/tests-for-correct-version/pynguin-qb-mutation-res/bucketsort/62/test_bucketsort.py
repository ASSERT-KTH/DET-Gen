# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -401
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    module_0.bucketsort(dict_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)


def test_case_2():
    int_0 = -401
    dict_0 = {}
    var_0 = module_0.bucketsort(dict_0, int_0)


def test_case_3():
    int_0 = -375
    dict_0 = {}
    var_0 = module_0.bucketsort(dict_0, int_0)
    bool_0 = True
    var_1 = module_0.bucketsort(var_0, bool_0)