# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2189 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 2004.99819
    module_0.func(*float_0)


def test_case_1():
    bytes_0 = b"\x12q\x0c"
    var_0 = module_0.func(*bytes_0)


def test_case_2():
    bytes_0 = b"\x12q\x0c"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xe7\x90L"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 20
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
