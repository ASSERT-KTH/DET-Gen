# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 798
    bool_0 = False
    tuple_0 = (int_0, int_0, bool_0)
    module_0.bucketsort(tuple_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1017
    dict_0 = {}
    var_0 = module_0.bucketsort(dict_0, int_0)
    module_0.bucketsort(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 972
    dict_0 = {}
    var_0 = module_0.bucketsort(dict_0, int_0)
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)