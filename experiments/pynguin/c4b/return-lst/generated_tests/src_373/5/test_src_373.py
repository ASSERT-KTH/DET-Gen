# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_373 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "8\x0c?*VAW{L\x0c=xZ"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '3f5\x0c}iYk;"'
    module_0.func(*str_0)


def test_case_3():
    str_0 = "9\x0c-8\x0c?*VW{L\x0c=xZ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "9\x0c-89\x0c?*VW{L=xZ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
