# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import to_base as module_0
import re as module_1


def test_case_0():
    int_0 = 613
    var_0 = module_0.to_base(int_0, int_0)
    assert var_0 == "10"


def test_case_1():
    bool_0 = False
    var_0 = module_0.to_base(bool_0, bool_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_2():
    var_0 = module_1.purge()
    module_1.sub(var_0, var_0, var_0)