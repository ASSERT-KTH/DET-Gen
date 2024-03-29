# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    bytes_0 = b"\xd9\x01\xf4\x95\xbc\xdcU\x10k\x8c\xddb\xf2>x\x1b\x99\x86"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 18
    var_1 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_1 == 18


def test_case_1():
    str_0 = "]`jeITT8hx~7;JN"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 15
    dict_0 = {}
    var_1 = module_0.lcs_length(dict_0, dict_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Z0#_\n"
    none_type_0 = None
    module_0.lcs_length(str_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    module_0.lcs_length(bool_0, bool_0)
