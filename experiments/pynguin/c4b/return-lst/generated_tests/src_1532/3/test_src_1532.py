# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1532 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"qn\xfa\xbd9\xd5\x0c"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -2053.052476209727
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xbf\x9f\xf9\x05\x14\x82\xdc\x06\x9d]"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -2050.4358912341163
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0, float_0]
    int_0 = 314
    list_1 = [int_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -2050.4358912341163
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0, float_0]
    int_0 = 314
    list_1 = [int_0, list_0]
    list_2 = [int_0, list_1, list_1, list_1]
    module_0.func(*list_2)


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = -2051.367234
    list_0 = [float_0, float_0, float_0, float_0, float_0]
    int_0 = 2
    list_1 = [
        list_0,
        int_0,
        float_0,
        list_0,
        float_0,
        list_0,
        list_0,
        list_0,
        float_0,
        int_0,
        list_0,
    ]
    var_0 = module_0.func(*list_0)
    list_2 = [int_0, list_1, float_0, list_1, var_0, var_0]
    var_1 = module_0.func(*list_2)
    module_0.func()