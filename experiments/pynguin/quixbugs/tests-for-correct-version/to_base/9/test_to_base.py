# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.to_base(bool_0, none_type_0)
    assert var_0 == ""
    int_0 = 2169
    module_0.to_base(int_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    var_0 = module_0.to_base(bool_0, bool_0)
    assert var_0 == ""
    module_0.to_base(var_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -633.529476
    list_0 = [float_0, float_0]
    module_0.to_base(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    regex_flag_0 = module_1.RegexFlag.IGNORECASE
    none_type_0 = None
    var_0 = module_0.to_base(bool_0, regex_flag_0)
    assert var_0 == "1"
    module_0.to_base(regex_flag_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    regex_flag_0 = module_1.RegexFlag.IGNORECASE
    var_0 = module_0.to_base(regex_flag_0, regex_flag_0)
    assert var_0 == "10"
    none_type_0 = None
    var_1 = module_0.to_base(bool_0, regex_flag_0)
    assert var_1 == "1"
    module_0.to_base(none_type_0, var_1)
