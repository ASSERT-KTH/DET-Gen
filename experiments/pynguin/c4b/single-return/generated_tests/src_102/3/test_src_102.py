# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_102 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bool_1 = True
    tuple_0 = (bool_0, bool_1)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 0
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
