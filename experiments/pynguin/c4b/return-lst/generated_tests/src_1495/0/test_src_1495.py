# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1495 as module_0


def test_case_0():
    str_0 = "mIgq{T(GMPx-"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -404
    module_0.func(*int_0)


def test_case_2():
    bytes_0 = b"\\i\xf6\xce{I\xd5\xfeP@\x06\xaa\xdaPN%"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa8\x18\x02(!\x87\xc18\x804\x850W:\xbc"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    int_0 = -1662
    module_0.func(*int_0)