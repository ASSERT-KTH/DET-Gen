# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1842 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "n\roKI(kP7"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "1\x0b2"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "1\x0b6"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "0\x0b2"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "0\x0b0"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)
