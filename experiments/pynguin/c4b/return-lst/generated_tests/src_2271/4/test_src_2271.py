# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2271 as module_0


def test_case_0():
    str_0 = "G,\x0bsRaWnb`pT`py`d%"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    str_0 = "G,\x0bsRaWnb`pT`pyBd%"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "G\x0bRO{n`p``p``"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    list_1 = [list_0, str_0]
    var_0 = module_0.func(*list_1)
