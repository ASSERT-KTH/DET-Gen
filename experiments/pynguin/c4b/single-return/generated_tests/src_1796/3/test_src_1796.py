# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1796 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"6\xb4\xea\xe4\x10\xf0\x8b\x14o"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 378
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 1802.30761
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3150
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 1801.2387447865015
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3150
    bytes_0 = b"\xd0\x16\x03\xf5\x95ln\x97\xe3{"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\xd46\xb4\xea *A\xe4\xbd\xf0Q'o"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 189
    module_0.func()
