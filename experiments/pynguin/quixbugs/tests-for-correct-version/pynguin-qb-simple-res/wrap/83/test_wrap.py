# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"1\n"
    float_0 = -2651.16261
    module_0.wrap(bytes_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.wrap(none_type_0, none_type_0)


def test_case_2():
    bytes_0 = b"1"
    float_0 = 3776.0001
    var_0 = module_0.wrap(bytes_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    str_0 = "x7tHX\n6Rv"
    var_0 = module_0.wrap(str_0, bool_0)
    module_0.wrap(bool_0, str_0)