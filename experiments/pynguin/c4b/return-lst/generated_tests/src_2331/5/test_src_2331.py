# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2331 as module_0


def test_case_0():
    str_0 = "?"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "3}~4cQ7D\t=J\x0c"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "9"
    list_0 = [str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "HZ=\\i*N6-Y=h* )"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)
