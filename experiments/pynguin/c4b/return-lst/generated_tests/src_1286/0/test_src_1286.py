# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1286 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "@bWBK\x0b6AX7\rPoTn]KD"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "@bWBK\x0b6AX7\rPoTn]KD"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ";|H-$e<Y6\x0c>g-s,v\tQ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "Ydn6II"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "|H-$e<Y6\x0c>g-s,v\tQ"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = ""
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    float_0 = -811.0
    list_0 = [float_0, float_0]
    list_1 = [list_0, list_0, list_0, list_0]
    bytes_0 = b"\xe3K\xf5\x11\xc1\xd3:\xc9`\xb8\x80\xa3\x00\xb6\x8f\x9a\x13\xa9\xb5"
    list_2 = [list_1, list_0, bytes_0]
    var_0 = module_0.func(*list_2)
    module_0.func()
