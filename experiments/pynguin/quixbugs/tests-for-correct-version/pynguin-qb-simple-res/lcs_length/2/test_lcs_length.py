# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 825
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 4
    module_0.lcs_length(int_0, int_0)


def test_case_1():
    str_0 = "v\x0b;vR_)/KnJK)~`-"
    str_1 = '4E"FUH^j{Tm'
    var_0 = module_0.lcs_length(str_0, str_1)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)