# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1741
    module_0.longest_common_subsequence(int_0, int_0)


def test_case_1():
    bytes_0 = b"@x"
    str_0 = "@,\t!"
    bool_0 = True
    tuple_0 = (bytes_0, str_0, bool_0)
    var_0 = module_0.longest_common_subsequence(tuple_0, bytes_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(bool_0, none_type_0)
    assert var_0 == ""
    var_1 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_1 == ""
    bytes_0 = b"\xef)\xe0\xf0\xfc\xeca\x99\xbbE\xc5u"
    module_0.longest_common_subsequence(bytes_0, bytes_0)