# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import pascal as module_0


def test_case_0():
    bool_0 = False
    var_0 = module_0.pascal(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = -4939.090557 - 943.5276j
    module_0.pascal(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 349
    var_0 = module_0.pascal(int_0)
    none_type_0 = None
    module_0.pascal(none_type_0)