# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1532 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 0
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xdb\x18\xef\x9c\xaf\xc5\xf7.\xb2,N\x89\x04(#K\xbb"
    float_0 = 479.095
    list_0 = [float_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    float_0 = 479.095
    list_1 = [float_0, list_0, list_0, var_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bytes_0 = b"~\xdd\xef/\xb1\xf3e\x15\xda\xdcW\\\xb5y*\xc1M\xf6\x84\x1e"
    float_0 = 13.47532633705206
    list_1 = [float_0, bytes_0, float_0, bool_0, bool_0, float_0, float_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 0
    module_0.func(*var_1)
