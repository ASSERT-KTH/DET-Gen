# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


def test_case_0():
    tuple_0 = ()
    var_0 = module_0.flatten(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa6\x1f!~u\xf0\xe9\xa6q\xed\x1a\xd5v"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    var_0 = module_0.flatten(none_type_0)
    var_1 = module_0.flatten(var_0)
    float_0 = 1482.0
    list_0 = [float_0, float_0, float_0]
    tuple_0 = (list_0,)
    var_2 = module_0.flatten(tuple_0)
    var_3 = module_0.flatten(var_0)
    int_0 = -1361
    var_4 = module_0.flatten(float_0)
    var_5 = module_0.flatten(int_0)
    var_6 = module_0.flatten(var_0)
    var_7 = module_0.flatten(var_5)
    bool_0 = True
    var_8 = module_0.flatten(var_0)
    var_9 = module_0.flatten(bool_0)
    dict_0 = {var_0: list_0, var_5: int_0}
    module_1.object(*var_2, **dict_0)
