# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    module_0.wrap(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1321.87
    tuple_0 = (float_0,)
    var_0 = module_0.wrap(tuple_0, float_0)
    module_0.wrap(float_0, var_0)


def test_case_2():
    str_0 = "u9\x0c-:B[A)CH-Z3w"
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)
    object_0 = module_1.object()
