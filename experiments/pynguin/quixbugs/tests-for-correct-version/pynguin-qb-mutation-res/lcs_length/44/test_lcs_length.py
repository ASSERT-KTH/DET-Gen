# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 153.923965
    list_0 = [float_0]
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 1
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.lcs_length(set_0, set_0)
    assert var_0 == 0
    var_1 = module_0.lcs_length(set_0, set_0)
    assert var_1 == 0
    str_0 = "`>jfh"
    var_2 = module_0.lcs_length(str_0, str_0)
    assert var_2 == 5
    module_0.lcs_length(var_1, var_2)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"7\x9c\xf7\xe9\xdal\xde\xb2O\xcd\xd4\x99"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.lcs_length(dict_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    module_0.lcs_length(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xe5~"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 2
    bool_0 = False
    module_0.lcs_length(bool_0, bool_0)