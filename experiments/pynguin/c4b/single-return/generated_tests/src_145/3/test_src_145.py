# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0


def test_case_0():
    int_0 = -1702
    str_0 = "2L0rE,?S!;qdEc]6eqO"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1108.2472
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 41.39283
    dict_0 = {float_0: float_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 1
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 3123.7712
    bool_0 = False
    float_1 = 41.39283
    dict_0 = {}
    tuple_0 = (bool_0, float_1, dict_0)
    list_0 = [float_0, tuple_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    list_1 = [var_0, var_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    module_0.func()
