# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lis as module_0


def test_case_0():
    bytes_0 = b"\x1d\xa7\xbb\xf8\xc4\xef6"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 5


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = -708.26779 - 1271.5367j
    module_0.lis(complex_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"*\xaf\\\x938\xcb\xaa\xf7p*9v"
    var_0 = module_0.lis(bytes_0)
    assert var_0 == 5
    str_0 = 'M"s8k$!WwbyG}!_L7bX@'
    var_1 = module_0.lis(str_0)
    assert var_1 == 6
    var_2 = module_0.lis(str_0)
    assert var_2 == 6
    module_0.lis(var_2)