# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2592 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "u_StkWA\x0b/C7\x0cN L-v"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "E\nF:v% 7:S7z"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "99H99999999999"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "99999999999999"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    float_0 = -121.3547
    int_0 = -2644
    tuple_0 = (float_0, int_0, int_0)
    list_1 = [tuple_0, tuple_0, int_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "99999/9999999"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    var_1 = module_1.object()
    module_0.func()