# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 2776.683949
    module_0.hanoi(float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1561
    none_type_0 = None
    var_0 = module_0.hanoi(int_0, none_type_0)
    object_0 = module_1.object()
    module_0.hanoi(object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.hanoi(none_type_0, end=none_type_0)