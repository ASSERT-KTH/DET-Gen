# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    str_0 = "w8RAp_\tk?jqs*tr89!#"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 19


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    list_1 = [list_0]
    str_0 = "b9F"
    tuple_0 = (list_1, str_0)
    var_0 = module_0.lcs_length(tuple_0, str_0)
    assert var_0 == 0
    bool_1 = False
    module_0.lcs_length(bool_1, bool_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.lcs_length(bool_0, bool_0)