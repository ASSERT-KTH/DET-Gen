# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    bytes_0 = b"!\x13\xcd\xa1n\x1c\x8fTG"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 3


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    module_0.lis(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 2359
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.lis(list_0)
    assert var_0 == 1
    list_1 = []
    var_1 = module_0.lis(list_1)
    assert var_1 == 0
    var_2 = module_0.lis(list_1)
    assert var_2 == 0
    var_3 = module_0.lis(list_1)
    assert var_3 == 0
    module_0.lis(var_1)