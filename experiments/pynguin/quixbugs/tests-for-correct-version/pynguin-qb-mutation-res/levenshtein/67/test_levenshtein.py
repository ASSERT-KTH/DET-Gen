# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import levenshtein as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb1\x12\xd3\x92\x1a\xaaF\xca"
    module_0.levenshtein(bytes_0, bytes_0)


def test_case_1():
    str_0 = "u\x0bb_H&I@fH"
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'\x80\xa7I\xae\x15"\x8f;\x8f\xa8\t\xe2'
    str_0 = "u\x0bb_H&I@fH"
    tuple_0 = (bytes_0, str_0)
    var_0 = module_0.levenshtein(str_0, str_0)
    assert var_0 == 0
    module_0.levenshtein(tuple_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'\x80\xa7I\xae\x15"\x8f;\x8f\xa8\t\xe2'
    str_0 = "\x0bn)H\\b7\t%P"
    module_0.levenshtein(bytes_0, str_0)