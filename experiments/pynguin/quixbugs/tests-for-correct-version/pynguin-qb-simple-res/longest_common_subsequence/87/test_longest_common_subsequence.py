# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1074.555
    module_0.longest_common_subsequence(float_0, float_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.longest_common_subsequence(bool_0, bool_0)
    assert var_0 == ""


def test_case_2():
    int_0 = -1484
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(int_0, none_type_0)
    assert var_0 == ""
    str_0 = '3O#nf;4i5"\\)~v'
    var_1 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_1 == '3O#nf;4i5"\\)~v'
    bool_0 = False
    var_2 = module_0.longest_common_subsequence(bool_0, bool_0)
    assert var_2 == ""


def test_case_3():
    str_0 = "T,==%"
    var_0 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_0 == "T,==%"
    var_1 = module_0.longest_common_subsequence(str_0, var_0)
    assert var_1 == "T,==%"
    var_2 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_2 == "T,==%"
    var_3 = module_0.longest_common_subsequence(var_0, var_0)
    assert var_3 == "T,==%"
    var_4 = module_0.longest_common_subsequence(var_0, str_0)
    assert var_4 == "T,==%"
    var_5 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_5 == "T,==%"
    bytes_0 = b"\x10lj\xe5d\xb6>\x1b\xed\x86\xc1\xe5W\xb5Z\x9fH+"
    var_6 = module_0.longest_common_subsequence(bytes_0, var_4)
    assert var_6 == ""
    var_7 = module_0.longest_common_subsequence(str_0, var_6)
    assert var_7 == ""
    none_type_0 = None
    var_8 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_8 == ""