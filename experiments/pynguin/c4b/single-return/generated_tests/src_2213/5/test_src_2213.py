# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2213 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*list_0)
    assert var_1 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 735
    str_0 = "Cg$>fxDVyV\x0b%iE\rHT~"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 736
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1185
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1184
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 756
    str_0 = "Cg$>fxDVyV\x0b%iE\rHT~"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 758
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 3440
    str_0 = "Cg$>fxDVyVQ%iE\rHT~"
    list_0 = [int_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3450
    module_0.func()
