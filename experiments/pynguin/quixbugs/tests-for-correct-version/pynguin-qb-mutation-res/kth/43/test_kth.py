# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1880.72
    bool_0 = False
    tuple_0 = (bool_0,)
    tuple_1 = (float_0, tuple_0)
    list_0 = [tuple_1]
    module_0.kth(list_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "M(?w{$ET{^v5\nL%u"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.kth(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -1294.263322
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0]
    module_0.kth(list_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    bool_1 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_1: bool_0, bool_0: bool_0}
    var_0 = module_0.kth(dict_0, bool_1)
    assert var_0 is False
    module_0.kth(bool_1, var_0)