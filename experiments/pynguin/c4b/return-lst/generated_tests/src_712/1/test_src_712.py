# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_712 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "9f]$q"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = 1396.2214
    bool_0 = True
    bool_1 = False
    tuple_0 = (float_0, bool_0, bool_0, bool_1)
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
