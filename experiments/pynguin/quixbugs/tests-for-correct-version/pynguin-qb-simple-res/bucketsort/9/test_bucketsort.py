# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -3728
    dict_0 = {int_0: int_0, int_0: int_0}
    int_1 = 986
    module_0.bucketsort(dict_0, int_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xc6&"
    module_0.bucketsort(bytes_0, bytes_0)


def test_case_2():
    int_0 = 986
    set_0 = set()
    var_0 = module_0.bucketsort(set_0, int_0)