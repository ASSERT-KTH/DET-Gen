# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    float_0 = 1456.761039
    tuple_0 = (bool_0, float_0)
    var_0 = module_0.max_sublist_sum(tuple_0)
    assert var_0 == pytest.approx(1457.761039, abs=0.01, rel=0.01)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.max_sublist_sum(object_0)