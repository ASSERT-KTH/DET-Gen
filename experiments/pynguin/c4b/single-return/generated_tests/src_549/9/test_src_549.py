# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_549 as module_0


def test_case_0():
    str_0 = "5SGBtB7Fl@\n&xEa\n="
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"\x12\\\xea\xc2a \x82\xb4?\xcex!\xdfg\xcf8\xb4\xdeU"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4


def test_case_3():
    bytes_0 = b"\x14\xad\xb5\x0e\x99Sc\xa3\x9b\x97\xe3j5\xba"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 15
