# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1652 as module_0


def test_case_0():
    float_0 = -341.2757063154061
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xdej\xd9\xb7hrf?\xbc\xc5\x8b\xf3\xd7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 50
    float_0 = -330.9335
    list_0 = [float_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    module_0.func()
