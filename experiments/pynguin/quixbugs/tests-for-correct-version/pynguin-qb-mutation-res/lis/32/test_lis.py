# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    bytes_0 = b"\xf7\xe4n\xfa["
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 2


def test_case_1():
    dict_0 = {}
    var_0 = module_0.lis(dict_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    var_0 = module_0.lis(list_0)
    assert var_0 == 0
    str_0 = "uW89T4Ik4Rv)9Sx"
    var_1 = module_0.lis(str_0)
    assert var_1 == 6
    var_2 = module_0.lis(str_0)
    assert var_2 == 6
    var_3 = module_0.lis(list_0)
    module_0.lis(var_2)