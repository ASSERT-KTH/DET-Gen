# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1799 as module_0
import builtins as module_1


def test_case_0():
    float_0 = 320.44
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x99E\xeb\xfd\xe6\xba\xac\xe0\x94"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*bytes_0)
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    var_2 = module_0.func(*list_0)
    module_0.func()
