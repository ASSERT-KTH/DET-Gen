# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2339 as module_0


def test_case_0():
    str_0 = "+^6H\\e<u6m)_X}N4Y6\nL"
    int_0 = 17
    str_1 = "}^%6(;:_gGS?\x0b).;}F"
    tuple_0 = (int_0, str_0, str_1)
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, tuple_0: tuple_0}
    list_0 = [str_0, dict_0, int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    list_0 = [set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ",<r>+]G>^*"
    var_0 = module_0.func(*str_0)
    module_0.func()
