# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2590 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "7"
    var_1 = module_0.func(*list_0)
    assert var_1 == "7"
    var_2 = module_0.func(*var_1)
    assert var_2 == "711"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 936
    dict_0 = {int_0: int_0, int_0: int_0}
    set_0 = {int_0, int_0, int_0}
    list_0 = [int_0, dict_0, dict_0, set_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
    bool_0 = True
    list_1 = [bool_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "7"
    var_2 = module_0.func(*list_1)
    assert var_2 == "7"
    var_3 = module_0.func(*var_2)
    assert var_3 == "711"
    module_1.object(**list_1)
