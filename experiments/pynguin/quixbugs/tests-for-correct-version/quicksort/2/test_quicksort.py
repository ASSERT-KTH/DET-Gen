# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 767
    module_0.quicksort(int_0)


def test_case_1():
    bytes_0 = b"\xe4\xb8\xf8\x05\xca0\xaf\x8b\x8c\xf5\t\xda9\xf2\x0e\x92\x9c\x03\x0fx"
    var_0 = module_0.quicksort(bytes_0)
