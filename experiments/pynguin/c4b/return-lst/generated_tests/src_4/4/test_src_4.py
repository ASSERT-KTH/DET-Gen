# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_4 as module_0


def test_case_0():
    bytes_0 = b"#\x18\x93\x964\xf1dwb\x18\xbe"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    float_0 = -2304.0
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'"\x83\xc41y'
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b'"\x83\xc41y'
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b'"\x83\xc41y'
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_2)
    module_0.func()