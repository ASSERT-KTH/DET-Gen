# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 1709
    bool_0 = True
    bool_1 = True
    var_0 = module_0.subsequences(bool_0, int_0, bool_1)
    bytes_0 = b"\xb4\x93K]\xf1\x80\x01\xc8\x013\xc2\xa0>a\xcaY\x93\x12\xf61"
    str_0 = "<`/IX"
    tuple_0 = (bytes_0, str_0)
    module_0.subsequences(tuple_0, bytes_0, bytes_0)


def test_case_1():
    int_0 = 1722
    var_0 = module_0.subsequences(int_0, int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -4063
    module_0.subsequences(int_0, int_0, int_0)