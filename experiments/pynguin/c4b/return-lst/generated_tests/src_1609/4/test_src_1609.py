# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1609 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"\x07\xd9\x9c|\xb2\xf7\xc4\xd9@\x12\xaa\xc2\xbe~\x81\x11\x8b\xbd\xc9\x0c"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xb7\x07\xfb\xd9\xaa\xc2d~\x81\x11\x8b\xbdP\x0c"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x07\xfb\xd9\xaa\xc2\xdf~\x81\x11\x8b\xbd\xc9\x0c"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


def test_case_4():
    float_0 = -1703.53693
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 1645.2
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x04\xf0"
    var_0 = module_0.func(*bytes_0)
    module_1.object(**var_0)
