# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1089 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 864
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa7Y/\x15\x7f\xce\x17|"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
