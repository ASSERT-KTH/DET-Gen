# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_916 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = ' k{Ai5SRy7\x0cn;"X\\Qz'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 9
    list_1 = [str_0, str_0, str_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 9


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "+\x0b)&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()
