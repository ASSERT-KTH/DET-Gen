# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2595 as module_0


def test_case_0():
    int_0 = 577
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    str_0 = "?VLC 8Sq"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
