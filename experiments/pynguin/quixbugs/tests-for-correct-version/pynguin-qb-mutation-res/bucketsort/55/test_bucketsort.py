# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


def test_case_0():
    int_0 = 5077
    bytes_0 = b"\x12q\x0f\xc9"
    var_0 = module_0.bucketsort(bytes_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.bucketsort(bool_0, bool_0)