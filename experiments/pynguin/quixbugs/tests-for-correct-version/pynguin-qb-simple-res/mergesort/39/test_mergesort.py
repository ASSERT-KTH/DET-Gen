# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mergesort as module_0


def test_case_0():
    bytes_0 = b"\x95\xd6\xadQ\x07\xe9\\\xe3.\x82O\xff\x070\xb6\xc0"
    var_0 = module_0.mergesort(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.mergesort(none_type_0)