# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_854 as module_0
import builtins as module_1


def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1851.0701774140416
    list_0 = [float_0]
    module_0.func(*list_0)


def test_case_2():
    object_0 = module_1.object()
    list_0 = [object_0, object_0]
    module_0.func(*list_0)
    var_0 = module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "c8Y\t"
    bool_0 = True
    var_0 = module_0.func(*str_0)
    set_0 = {bool_0, bool_0}
    tuple_0 = (str_0, bool_0, set_0)
    float_0 = 1847.447439533415
    list_0 = [float_0, float_0, bool_0, tuple_0, bool_0]
    var_1 = module_0.func(*list_0)
    module_0.func()
