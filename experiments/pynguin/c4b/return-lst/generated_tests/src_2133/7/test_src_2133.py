# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2133 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"*\xa7\n\x12\xa7"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1121
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
