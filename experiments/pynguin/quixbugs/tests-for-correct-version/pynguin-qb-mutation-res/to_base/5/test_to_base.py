# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    module_0.to_base(bool_0, list_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.to_base(bool_0, bool_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    regex_flag_0 = module_1.RegexFlag.DEBUG
    var_0 = module_0.to_base(regex_flag_0, regex_flag_0)
    assert var_0 == "10"
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)