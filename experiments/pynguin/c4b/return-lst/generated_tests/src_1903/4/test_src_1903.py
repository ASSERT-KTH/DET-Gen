# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1903 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "?Jl55\nu8Dir\n"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "g^#jh\\]O,h=9F"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    float_0 = -1854.35
    list_0 = [float_0, float_0, float_0]
    list_1 = [list_0, float_0]
    var_0 = module_0.func(*list_1)


def test_case_3():
    list_0 = []
    list_1 = [list_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    str_0 = "g^#jh\\]O,h=9F"
    list_2 = [str_0, str_0]
    var_1 = module_0.func(*list_2)
    var_2 = module_0.func(*list_2)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -1828.109412357472
    complex_0 = 2619.230631 - 767.9j
    list_0 = [
        float_0,
        float_0,
        float_0,
        float_0,
        float_0,
        float_0,
        float_0,
        complex_0,
        complex_0,
        complex_0,
        complex_0,
        complex_0,
        complex_0,
    ]
    list_1 = [list_0, complex_0]
    var_0 = module_0.func(*list_1)
    module_1.object(*list_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = -1854.35
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0, float_0]
    dict_0 = {float_0: float_0, float_0: list_0, float_0: list_0, float_0: list_0}
    list_1 = [list_0, dict_0]
    var_0 = module_0.func(*list_1)
    module_0.func()
