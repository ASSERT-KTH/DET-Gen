# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import pascal as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 338
    var_0 = module_0.pascal(int_0)
    bool_0 = True
    var_1 = module_0.pascal(int_0)
    var_2 = module_0.pascal(bool_0)
    module_0.pascal(var_2)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -945
    var_0 = module_0.pascal(int_0)
    module_0.pascal(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '?2]"T7d!WDU&Y<'
    module_0.pascal(str_0)