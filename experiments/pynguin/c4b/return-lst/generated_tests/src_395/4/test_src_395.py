# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_395 as module_0


def test_case_0():
    bytes_0 = b"\x15\x94"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"\x15\x94"
    var_0 = module_0.func(*bytes_0)


def test_case_3():
    float_0 = 684.6864672953752
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x0f\x87r,~U\xc2\x8a\r\xed\xbf\x10va\xccw\xf9#"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x14\x94"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    module_0.func()