# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1035 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    bool_1 = True
    var_1 = module_0.func(*list_0)
    assert var_1 == 5
    module_0.func(*bool_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 4010
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 25
    list_1 = [int_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 25
    module_0.func()
