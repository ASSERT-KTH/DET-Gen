# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.possible_change(bool_0, bool_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.possible_change(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -259
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    set_0 = {int_0, int_0, int_0, int_0}
    set_1 = set()
    module_0.possible_change(set_1, set_0)


def test_case_3():
    none_type_0 = None
    int_0 = 614
    var_0 = module_0.possible_change(none_type_0, int_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    module_0.possible_change(bool_0, bool_0)