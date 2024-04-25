# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"d\\r\x84\x7f2\xbf\xe8dEf\xfb\xed\x18\xb8\xd0"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 16
    set_0 = {bytes_0, bytes_0, bytes_0}
    module_0.lcs_length(bytes_0, set_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 0
    var_1 = module_0.lcs_length(list_0, list_0)
    assert var_1 == 0
    bytes_0 = b"\xcc4\xc9klc(\xef\x18\x0c\xa3\xa0c*(\x88\x13"
    bytes_1 = b"\xecO2v"
    var_2 = module_0.lcs_length(bytes_1, bytes_1)
    assert var_2 == 4
    var_3 = module_0.lcs_length(bytes_0, bytes_1)
    assert var_3 == 0
    var_4 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_4 == 17


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    tuple_0 = (bool_0,)
    dict_0 = {tuple_0: tuple_0, bool_0: tuple_0, bool_0: bool_0}
    none_type_0 = None
    module_0.lcs_length(dict_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    module_0.lcs_length(bool_0, bool_0)