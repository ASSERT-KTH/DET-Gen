# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1453 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xef\xcb\xff\xe0\xb2\xd3\xa2Q\xc3\xbd\x80H\x18\xae"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"~\xd8\xe5\xd9\xb2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 1
    var_2 = module_0.func(*bytes_0)
    assert var_2 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x9c\x1f\x18N\xe6\x15\xe2\xb4xX7\xbe\xbf\x10"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 18
    var_1 = module_1.object()
    module_0.func()
