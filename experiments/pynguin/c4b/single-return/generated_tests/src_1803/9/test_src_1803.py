# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1803 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "@\\\rHo|%at'sY"
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "xRCC\r#rX{l w1\n)$\x0bD+E"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -3757
    list_0 = [int_0, int_0, int_0, int_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1
    module_0.func()