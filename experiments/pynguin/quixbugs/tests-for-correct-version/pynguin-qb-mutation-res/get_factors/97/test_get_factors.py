# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import get_factors as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bytes_0 = b"\xb7\x9bd\x8a\x1f\xd0}\x1c"
    dict_0 = {bool_0: bool_0, bytes_0: bytes_0, bool_0: bool_0}
    var_0 = module_0.get_factors(bool_0)
    var_1 = module_0.get_factors(bool_0)
    module_0.get_factors(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.get_factors(none_type_0)


def test_case_2():
    int_0 = 1647
    var_0 = module_0.get_factors(int_0)