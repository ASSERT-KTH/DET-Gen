# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import possible_change as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -4165
    bool_0 = True
    set_0 = {int_0, int_0, bool_0}
    module_0.possible_change(set_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\x0b7:"
    set_0 = {str_0}
    module_0.possible_change(set_0, set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -861
    var_0 = module_0.possible_change(int_0, int_0)
    assert var_0 == 0
    list_0 = []
    module_0.possible_change(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf5"
    float_0 = 703.6653
    var_0 = module_0.possible_change(bytes_0, float_0)
    assert var_0 == 0
    module_0.possible_change(var_0, bytes_0)