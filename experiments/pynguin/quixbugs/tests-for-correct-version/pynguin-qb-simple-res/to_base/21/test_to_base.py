# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 233
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"
    var_1 = module_0.to_base(int_0, int_0)
    assert var_1 == "10"
    module_0.to_base(int_0, var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -2125
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == ""
    bytes_0 = b"?0\x11\xa3O\x98\xbes\x95G?\x07\x1a\xa2\xf3\xed\x96"
    none_type_0 = None
    module_0.to_base(bytes_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.to_base(none_type_0, none_type_0)