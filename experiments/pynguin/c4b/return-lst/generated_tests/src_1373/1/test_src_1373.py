# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1373 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -614.477
    bool_0 = True
    list_0 = [float_0, bool_0, float_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -288.7715
    bool_0 = True
    list_0 = [float_0, bool_0, float_0]
    module_0.func(*list_0)
