# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_769 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 500.66
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1196
    bytes_0 = b",\x11T,\xecV\x1b\x93"
    list_0 = [int_0, bytes_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func(*object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
