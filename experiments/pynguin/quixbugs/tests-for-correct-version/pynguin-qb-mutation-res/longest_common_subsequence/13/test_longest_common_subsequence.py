# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    module_0.longest_common_subsequence(list_0, list_0)


def test_case_1():
    int_0 = -628
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(int_0, none_type_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(var_0, none_type_0)
    assert var_1 == ""
    str_0 = "v"
    var_2 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_2 == "v"
    var_3 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_3 == "v"
    var_4 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_4 == "v"


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "@\x0bAT/Fi"
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "@\x0bAT/Fi"
    var_1 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_1 == "@\x0bAT/Fi"
    var_2 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_2 == "@\x0bAT/Fi"
    var_3 = module_0.longest_common_subsequence(var_1, var_1)
    assert var_3 == "@\x0bAT/Fi"
    list_0 = [var_1, var_3, var_1, var_2]
    var_4 = module_0.longest_common_subsequence(str_0, list_0)
    assert var_4 == ""
    var_5 = module_0.longest_common_subsequence(var_1, var_4)
    assert var_5 == ""
    var_6 = module_0.longest_common_subsequence(str_0, var_0)
    assert var_6 == "@\x0bAT/Fi"
    var_7 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_7 == "@\x0bAT/Fi"
    var_8 = module_0.longest_common_subsequence(var_1, var_7)
    assert var_8 == "@\x0bAT/Fi"
    var_9 = module_0.longest_common_subsequence(var_1, var_3)
    assert var_9 == "@\x0bAT/Fi"
    var_10 = module_0.longest_common_subsequence(str_0, var_7)
    assert var_10 == "@\x0bAT/Fi"
    bool_0 = True
    module_0.longest_common_subsequence(bool_0, var_7)