# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mergesort as module_0


def test_case_0():
    bytes_0 = b"\xf1\xe7\xe7\xffF/\x8d\xb3\x7f\xc2"
    var_0 = module_0.mergesort(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.mergesort(bool_0)