# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


def test_case_0():
    float_0 = -2106.9
    list_0 = [float_0, float_0, float_0]
    bytes_0 = b"wnBr\x0f\x16\x02\tz\xfe\x03\xd7\xe1\xd38\x9e\xca6B\xcd"
    var_0 = module_0.longest_common_subsequence(list_0, bytes_0)
    assert var_0 == ""


def test_case_1():
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb5\x15\x9f\xbf\n\x18'\xf8a\xcbgm\xd3\xfa-"
    module_0.longest_common_subsequence(bytes_0, bytes_0)