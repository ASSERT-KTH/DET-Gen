# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_604 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "_9V7b\x0b\\VIfo"
    bool_0 = True
    list_0 = [str_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "7^b"
    module_0.func(*str_0)
