# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1493 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -2277.871
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -455
    var_1 = module_1.object()
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -1985
    tuple_0 = ()
    list_0 = [int_0, tuple_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -397
    module_0.func()
