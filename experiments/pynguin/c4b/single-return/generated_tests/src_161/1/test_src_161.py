# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_161 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = 350.27 - 4074j
    module_0.func(*complex_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
