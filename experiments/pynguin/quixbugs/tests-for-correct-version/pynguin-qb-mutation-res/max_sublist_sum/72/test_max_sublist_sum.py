# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import max_sublist_sum as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = -3848.422 + 2108j
    bytes_0 = b"\xd1\xd9S"
    var_0 = module_0.max_sublist_sum(bytes_0)
    assert var_0 == 509
    module_0.max_sublist_sum(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.max_sublist_sum(none_type_0)