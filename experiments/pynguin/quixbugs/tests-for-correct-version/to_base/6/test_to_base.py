# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 587
    none_type_0 = None
    module_0.to_base(int_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -77
    bool_0 = False
    var_0 = module_0.to_base(int_0, bool_0)
    assert var_0 == ""
    str_0 = "bb,<}?IqE) #l\nx6"
    set_0 = {str_0, str_0}
    none_type_0 = None
    set_0.__iter__(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 5129
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_1 = module_0.to_base(int_0, int_0)
    assert var_1 == "10"
    var_1.setdefault(var_1)
