# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'LY*:jQCsz9^1*#)7L"N'
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 19
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 0
    bytes_0 = b"\xe4\xee{\x9e\x98\x89\x90"
    var_1 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_1 == 7
    int_0 = -1723
    module_0.lcs_length(var_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "("
    none_type_0 = None
    module_0.lcs_length(str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)