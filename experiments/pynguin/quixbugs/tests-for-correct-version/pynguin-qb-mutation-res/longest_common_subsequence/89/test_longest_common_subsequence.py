# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -2162.60223
    module_0.longest_common_subsequence(float_0, float_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.longest_common_subsequence(bool_0, bool_0)
    assert var_0 == ""


def test_case_2():
    str_0 = "SVUI9tQ 9}r{P"
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, str_0)
    assert var_0 == ""
    str_1 = "Eg#xV8|,ck$jPQ "
    var_1 = module_0.longest_common_subsequence(str_1, var_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(str_0, str_0)
    assert var_2 == "SVUI9tQ 9}r{P"


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf8\xd6D\xba\x87\x10&\x12F|S\xf2\xaa\xcdV\x1a\xc0\\3"
    tuple_0 = (bytes_0,)
    var_0 = module_0.longest_common_subsequence(tuple_0, bytes_0)
    assert var_0 == ""
    bool_0 = False
    none_type_0 = None
    tuple_1 = ()
    var_1 = module_0.longest_common_subsequence(tuple_1, none_type_0)
    assert var_1 == ""
    var_2 = module_0.longest_common_subsequence(none_type_0, bool_0)
    assert var_2 == ""
    var_3 = module_0.longest_common_subsequence(none_type_0, tuple_1)
    assert var_3 == ""
    module_1.object(**var_1)