# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2531 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "3\x0c4"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "3\x0c4"
    str_1 = "~BhEqOb'(\x0cffsATrL"
    list_0 = [str_0, str_1]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "3\x0c4"
    str_1 = "~BG{hEqOb'(\x0cffsATrL"
    list_0 = [str_0, str_1, str_1, str_1]
    var_0 = module_0.func(*list_0)