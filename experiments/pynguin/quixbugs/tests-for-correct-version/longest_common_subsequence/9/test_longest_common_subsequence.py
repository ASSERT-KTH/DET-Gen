# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.longest_common_subsequence(bool_0, bool_0)


def test_case_1():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(bool_0, none_type_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_1 == ""


def test_case_2():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    var_0 = module_0.longest_common_subsequence(none_type_0, list_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_1 == ""
    list_1 = [list_0, list_0, none_type_0, var_1]
    var_2 = module_0.longest_common_subsequence(var_0, list_1)
    assert var_2 == ""
    var_3 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_3 == ""
    bytes_0 = b"\xba\x01t\x97\xd7\x86\xf8\xd7{0S\xc0}\xa5"
    var_4 = module_0.longest_common_subsequence(bytes_0, none_type_0)
    assert var_4 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    dict_0 = {}
    var_0 = module_0.longest_common_subsequence(dict_0, dict_0)
    assert var_0 == ""
    str_0 = "qr$Hq[Z;s1F2"
    tuple_0 = (str_0,)
    var_1 = module_0.longest_common_subsequence(tuple_0, str_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_2 == "qr$Hq[Z;s1F2"
    str_1 = " {"
    var_3 = module_0.longest_common_subsequence(str_1, str_1)
    assert var_3 == " {"
    var_4 = module_0.longest_common_subsequence(str_1, str_1)
    assert var_4 == " {"
    bool_0 = True
    module_0.longest_common_subsequence(bool_0, bool_0)
