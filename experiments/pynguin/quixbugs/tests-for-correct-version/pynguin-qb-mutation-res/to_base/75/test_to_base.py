# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    int_0 = 2276
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_1 = var_0.format(none_type_0)
    assert var_1 == "10"
    var_2 = module_1.compile(var_1)
    bool_0 = True
    module_1.Scanner(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1657
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == ""
    none_type_0 = None
    var_1 = module_0.to_base(int_0, none_type_0)
    assert var_1 == ""
    module_1.match(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)