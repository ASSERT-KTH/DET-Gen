# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2445 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "J"
    module_0.func(*str_0)


def test_case_1():
    str_0 = '#f}[{KS"\x0cX#\x0ce\nF\r'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ";\rq\x0cq"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)
