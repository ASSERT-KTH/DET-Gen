# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = 'NI"}uV.O+!ndd<.Q[L!'
    var_0 = module_0.lis(str_0)
    assert var_0 == 5
    var_1 = module_0.lis(str_0)
    assert var_1 == 5
    module_0.lis(var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.lis(set_0)
    assert var_0 == 0
    none_type_0 = None
    module_0.lis(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.lis(bool_0)