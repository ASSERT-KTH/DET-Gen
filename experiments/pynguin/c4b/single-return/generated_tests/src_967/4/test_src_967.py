# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_967 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"1%"
    list_0 = [bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"8 5"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 28


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"80 5"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 745
    module_0.func()
