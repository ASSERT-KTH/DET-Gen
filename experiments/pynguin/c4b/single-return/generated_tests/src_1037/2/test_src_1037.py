# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1037 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "V+"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -2082.6331
    list_0 = [float_0, float_0, float_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ""
    list_0 = [str_0, str_0, str_0]
    module_0.func(*list_0)
