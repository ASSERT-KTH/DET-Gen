# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1404 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -832
    list_0 = [int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 3015.588277
    list_0 = [float_0, float_0, float_0]
    module_0.func(*list_0)
