# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1354 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    int_0 = 374
    list_0 = [int_0, bool_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    int_0 = 339
    list_0 = [int_0, bool_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    list_1 = [bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    int_0 = 341
    list_0 = [int_0, int_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    list_1 = [bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    var_2 = module_0.func(*list_0)
    assert var_2 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 374
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    list_1 = [var_0, var_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
    module_0.func()