# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2212 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.func(*dict_0)
    module_0.func(*bool_0)


def test_case_1():
    int_0 = 788
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    module_0.func(*list_0)


def test_case_3():
    bool_0 = False
    dict_0 = {bool_0: bool_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -4001.28
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 3.88
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    float_0 = 2.5527372544905313
    list_0 = [float_0, float_0]
    bool_0 = True
    var_0 = module_0.func(*list_0)
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    module_1.object(*list_1)
