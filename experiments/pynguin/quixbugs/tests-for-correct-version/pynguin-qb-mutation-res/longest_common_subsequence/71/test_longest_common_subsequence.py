# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"5\xe9x\x12\xbfU4U\xdc\xda\xcd\xca\xdd"
    module_0.longest_common_subsequence(bytes_0, bytes_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.longest_common_subsequence(set_0, set_0)
    assert var_0 == ""


def test_case_2():
    int_0 = -642
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(int_0, none_type_0)
    assert var_0 == ""
    tuple_0 = ()
    var_1 = module_0.longest_common_subsequence(tuple_0, tuple_0)
    assert var_1 == ""


def test_case_3():
    bool_0 = False
    var_0 = module_0.longest_common_subsequence(bool_0, bool_0)
    assert var_0 == ""
    none_type_0 = None
    var_1 = module_0.longest_common_subsequence(var_0, bool_0)
    assert var_1 == ""
    str_0 = "iEU. "
    var_2 = module_0.longest_common_subsequence(bool_0, bool_0)
    assert var_2 == ""
    var_3 = module_0.longest_common_subsequence(var_0, bool_0)
    assert var_3 == ""
    var_4 = module_0.longest_common_subsequence(none_type_0, str_0)
    assert var_4 == ""
    var_5 = module_0.longest_common_subsequence(none_type_0, bool_0)
    assert var_5 == ""
    var_6 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_6 == ""
    str_1 = "ge:`<,~F}"
    bool_1 = False
    var_7 = module_0.longest_common_subsequence(var_6, bool_1)
    assert var_7 == ""
    var_8 = module_0.longest_common_subsequence(var_3, var_1)
    assert var_8 == ""
    bytes_0 = b"\x11\xa6"
    var_9 = module_0.longest_common_subsequence(str_1, bytes_0)
    assert var_9 == ""
    var_10 = module_0.longest_common_subsequence(none_type_0, str_1)
    assert var_10 == ""