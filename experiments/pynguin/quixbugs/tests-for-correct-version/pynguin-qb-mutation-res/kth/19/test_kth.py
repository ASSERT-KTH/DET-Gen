# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa4'\xdb\xc3\xb8\x05N\x08\xf6YKNu\xd7"
    module_0.kth(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    int_0 = 1013
    module_0.kth(list_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "3.T3r| "
    int_0 = -707
    module_0.kth(str_0, int_0)