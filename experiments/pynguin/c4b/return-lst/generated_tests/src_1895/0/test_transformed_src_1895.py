# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x92\x91\x9e"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1611.0
    list_0 = [float_0]
    list_1 = [list_0, float_0, float_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    tuple_0 = (bool_0, bool_0)
    list_0 = [tuple_0, bool_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    list_1 = [var_1, var_1, list_0, list_0]
    var_2 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    bool_1 = False
    list_0 = [tuple_0, bool_1]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, var_0, var_0, var_0]
    var_1 = module_0.func(*list_1)
#    module_1.object(*list_1)
