# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    module_0.longest_common_subsequence(bool_0, bool_0)


def test_case_1():
    str_0 = "]~WG?i^FVyY"
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "]~WG?i^FVyY"
    var_1 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_1 == "]~WG?i^FVyY"
    var_2 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_2 == "]~WG?i^FVyY"


def test_case_2():
    int_0 = 2354
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(int_0, none_type_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_1 == ""
    dict_0 = {}
    var_2 = module_0.longest_common_subsequence(dict_0, dict_0)
    assert var_2 == ""
    none_type_1 = None
    var_3 = module_0.longest_common_subsequence(none_type_1, none_type_1)
    assert var_3 == ""
    none_type_2 = None
    var_4 = module_0.longest_common_subsequence(none_type_2, none_type_2)
    assert var_4 == ""


def test_case_3():
    str_0 = "k\x0b'CjrO/Y]sKJ"
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "k\x0b'CjrO/Y]sKJ"
    none_type_0 = None
    var_1 = module_0.longest_common_subsequence(str_0, none_type_0)
    assert var_1 == ""
    list_0 = [str_0, str_0, str_0]
    var_2 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_2 == "k\x0b'CjrO/Y]sKJ"
    var_3 = module_0.longest_common_subsequence(var_2, list_0)
    assert var_3 == ""