# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -774
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(int_0, int_0)
    assert var_1 == 0
    var_2 = module_0.possible_change(int_0, int_0)
    assert var_2 == 0
    var_3 = module_0.possible_change(var_2, var_2)
    assert var_3 == 1
    var_4 = module_0.possible_change(var_2, var_1)
    assert var_4 == 1
    str_0 = ""
    list_0 = [str_0, var_1, var_4]
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    str_0 = "B+J}f1A}`WL{i\x0b>8Ly"
    module_0.possible_change(none_type_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.possible_change(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    bool_1 = True
    list_0 = [bool_1, bool_1, bool_1, bool_1]
    var_1 = module_0.possible_change(list_0, bool_1)
    assert var_1 == 4
    module_0.possible_change(bool_1, bool_1)
