# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1184 as module_0


def test_case_0():
    bytes_0 = b"\x88\x95\x85"
    var_0 = module_0.func(*bytes_0)


def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 1234567
    list_0 = [int_0]
    module_0.func(*list_0)
