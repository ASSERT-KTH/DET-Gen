# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1244
    module_0.longest_common_subsequence(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1330.195
    list_0 = [float_0]
    module_0.longest_common_subsequence(list_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1487.02
    tuple_0 = (float_0, float_0)
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(tuple_0, none_type_0)
    assert var_0 == ""
    bytes_0 = b"\xed&G\xce`)\xdc\xca>\xfcT\x17\xb8\xdf\x91\xdeQ\xf8^\xa2"
    module_0.longest_common_subsequence(bytes_0, bytes_0)


def test_case_3():
    bytes_0 = b"\x03F\\\xfal\x96\x9c\x06D\xf7\n\xd8\x93+\xb4\x9d\x8a\xe7\x18\xdd"
    complex_0 = -1003.2934 - 1368.601958j
    int_0 = 1903
    tuple_0 = (bytes_0, complex_0, int_0)
    var_0 = module_0.longest_common_subsequence(tuple_0, bytes_0)
    assert var_0 == ""
    str_0 = "-\\#K@B<"
    var_1 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_1 == "-\\#K@B<"
    var_2 = module_0.longest_common_subsequence(var_1, var_1)
    assert var_2 == "-\\#K@B<"