# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2575 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "1tB\r{;yqE7=lDp`~,\x0c8g"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "(I\x0cD(0}KKoB0sCM"
    bool_0 = False
    list_0 = [str_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func(*var_1)


def test_case_3():
    str_0 = "4GeJ!+ni< mU\x0bVVTL"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
