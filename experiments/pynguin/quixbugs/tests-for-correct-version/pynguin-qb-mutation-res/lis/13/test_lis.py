# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    str_0 = "6"
    var_0 = module_0.lis(str_0)
    assert var_0 == 1
    var_1 = module_0.lis(str_0)
    assert var_1 == 1


def test_case_1():
    str_0 = "Xk\\nASr#w)Yz$J;RK;qP"
    var_0 = module_0.lis(str_0)
    assert var_0 == 6
    bytes_0 = b"\xdc\xf7E\x82\x0cAjI\xaf5\xdf"
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_1 = module_0.lis(set_0)
    assert var_1 == 1
    var_2 = module_0.lis(set_0)
    assert var_2 == 1


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -380
    module_0.lis(int_0)