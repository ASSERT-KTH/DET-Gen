# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_558 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xdaK\rvPD\xa5\x891\xc5Df\xb6\xae\x0f"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    module_1.object(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xda\xc5K\rvPD\xa5\x891\xd0\xc5TDf\xb6\xae\x0f"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x075\xcc\xac\x88C"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 21
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xf3\xfaD\xe9B\x0b)\xd9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    list_0 = [var_0, var_0, var_0, var_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    module_0.func(*var_0)
