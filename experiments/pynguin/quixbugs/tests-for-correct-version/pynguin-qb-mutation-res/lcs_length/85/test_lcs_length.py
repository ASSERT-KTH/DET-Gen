# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "$kj2m"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 5
    var_1 = module_0.lcs_length(str_0, str_0)
    assert var_1 == 5
    module_0.lcs_length(str_0, var_1)


def test_case_1():
    set_0 = set()
    str_0 = "c>MccLx!S\t~`"
    tuple_0 = (set_0, str_0)
    var_0 = module_0.lcs_length(tuple_0, set_0)
    assert var_0 == 0