# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1517 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -876.0
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -439
    object_0 = module_1.object()
    list_1 = [object_0, object_0, object_0]
    module_0.func(*list_1)


def test_case_1():
    int_0 = 2737
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1368


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
