# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1
    module_0.possible_change(var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.possible_change(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2601
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    list_0 = [var_0]
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    int_0 = -1907
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    var_1 = module_0.possible_change(int_0, var_0)
    assert var_1 == 1
    var_2 = module_0.possible_change(var_0, var_1)
    assert var_2 == 0
    module_0.possible_change(bool_0, bool_0)