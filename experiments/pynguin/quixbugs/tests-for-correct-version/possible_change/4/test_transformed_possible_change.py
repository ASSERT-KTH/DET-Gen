# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    bool_0 = False
    var_0 = module_0.possible_change(none_type_0, bool_0)
    assert var_0 == 1


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -733
    dict_0 = {int_0: int_0}
    object_0 = module_1.object()
#    module_0.possible_change(dict_0, object_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1122.0
    var_0 = module_0.possible_change(float_0, float_0)
    assert var_0 == 0
    dict_0 = {}
#    module_0.possible_change(dict_0, dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 3376.0
#    module_0.possible_change(float_0, float_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 235
    tuple_0 = (int_0, int_0)
    int_1 = 81
    var_0 = module_0.possible_change(tuple_0, int_1)
    assert var_0 == 0
    tuple_1 = ()
#    module_0.possible_change(tuple_1, tuple_1)
