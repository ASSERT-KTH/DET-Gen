# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    int_0 = -2943
    module_0.kth(dict_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is False
    int_0 = -645
    module_0.kth(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -1734 + 5598.86909j
    module_0.kth(complex_0, complex_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x93\xaa\xfb|A\xc5p\xc2\xaf\t"
    bytes_1 = b"\xbe\xee\xa45{T@\xb7+m"
    module_0.kth(bytes_0, bytes_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    int_0 = 6020
    var_0 = module_0.kth(dict_0, bool_0)
    assert var_0 is False
    module_0.kth(dict_0, int_0)