# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2317 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "+ EFAvE|)o`BWsi"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = ";a|][88}"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -3612.592997505983
    tuple_0 = (float_0, float_0, float_0, float_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, float_0]
    list_1 = [list_0, tuple_0, list_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_0)
    module_1.object(*list_1, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -3585.53659275793
    tuple_0 = (float_0, float_0, float_0, float_0)
    list_0 = [float_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0]
    list_1 = [list_0, tuple_0, list_0, tuple_0]
    var_0 = module_0.func(*list_1)
    module_0.func()