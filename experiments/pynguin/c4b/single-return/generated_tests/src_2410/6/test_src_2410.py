# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2410 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 3123.91217
    tuple_0 = ()
    set_0 = {float_0, float_0, tuple_0, tuple_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "Leonard"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    object_0 = module_1.object()
    list_0 = [bool_0, object_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
    module_0.func(*var_0)
