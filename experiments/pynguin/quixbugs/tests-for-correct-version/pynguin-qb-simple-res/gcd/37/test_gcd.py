# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import gcd as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.gcd(bool_0, bool_0)
    assert var_0 is True
    none_type_0 = None
    module_0.gcd(bool_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xf2t?\xaf\x89\x95\x8aK\x03\xd6QUI\xc5$\x95"
    none_type_0 = None
    module_0.gcd(none_type_0, bytes_0)