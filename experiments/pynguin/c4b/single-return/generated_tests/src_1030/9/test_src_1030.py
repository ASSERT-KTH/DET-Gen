# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1030 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = 950.0514 + 2256.8274j
    module_0.func(*complex_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "yZIoi\tYiF["
    module_0.func(*str_0)
