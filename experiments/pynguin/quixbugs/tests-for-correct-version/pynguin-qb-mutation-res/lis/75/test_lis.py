# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "7e$mZITH,C"
    var_0 = module_0.lis(str_0)
    assert var_0 == 3
    var_1 = module_0.lis(str_0)
    assert var_1 == 3
    module_0.lis(var_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\x0cV+eS**"
    var_0 = module_0.lis(str_0)
    assert var_0 == 3
    none_type_0 = None
    module_0.lis(none_type_0)