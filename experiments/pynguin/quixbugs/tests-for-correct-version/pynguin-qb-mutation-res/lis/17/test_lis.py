# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "UU-Z$.T \t"
    var_0 = module_0.lis(str_0)
    assert var_0 == 3
    module_0.lis(var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.lis(none_type_0)