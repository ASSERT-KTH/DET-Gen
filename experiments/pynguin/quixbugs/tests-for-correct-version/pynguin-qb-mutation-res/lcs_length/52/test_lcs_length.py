# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"V\x1e\xc5\xf1D\x8c\tN\x82\x10"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 10
    module_0.lcs_length(var_0, var_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2375
    list_0 = [int_0]
    module_0.lcs_length(list_0, int_0)