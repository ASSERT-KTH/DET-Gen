# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "^k~%,R;l\x0c<GPF*V"
    var_0 = module_0.lis(str_0)
    assert var_0 == 7
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -2616.156
    module_0.lis(float_0)


def test_case_2():
    set_0 = set()
    var_0 = module_0.lis(set_0)
    assert var_0 == 0
    tuple_0 = (var_0, var_0, var_0, var_0)
    dict_0 = {var_0: var_0, var_0: set_0, var_0: tuple_0, tuple_0: var_0}
    var_1 = module_0.lis(dict_0)
    assert var_1 == 1
    var_2 = module_0.lis(set_0)
    assert var_2 == 0