# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 2818
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_0.get_value(var_0, var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.to_base(bool_0, bool_0)
    assert var_0 == ""
    var_1 = var_0.__iter__()
    module_1.findall(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)