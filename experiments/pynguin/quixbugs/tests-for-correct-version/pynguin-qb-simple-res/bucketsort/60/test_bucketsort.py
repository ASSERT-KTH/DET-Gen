# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "P|pJ"
    bool_0 = False
    module_0.bucketsort(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    module_0.bucketsort(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1336
    list_0 = []
    var_0 = module_0.bucketsort(list_0, int_0)
    module_0.bucketsort(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
    bool_0 = True
    var_0 = module_0.bucketsort(list_0, bool_0)
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)