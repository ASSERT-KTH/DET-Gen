# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1697 as module_0


def test_case_0():
    str_0 = '2(;H\nJl[XDI"iHf'
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '2(;H\nJl[XDI"Hf'
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()