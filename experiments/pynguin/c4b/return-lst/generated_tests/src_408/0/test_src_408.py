# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_408 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "@6EBaT&c~=B"
    module_0.func(*str_0)


def test_case_1():
    str_0 = "@6EBaT&c~=B"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    str_0 = "'Qk#4ms"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "\x0b+TTRK8bp+OHAS>|o$d"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "LT[.;8QiZs]`_V>"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
