# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_215 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    bytes_0 = b"\xbcB\xe5\x1d$\xe8h\xef\x91P\xa5\xb4|b\xe4F\xeb\x11\xfe"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    var_1 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x15\x08(\xd9\x16\x10\xb6\xa1\xd6\x81\x9b\x02\x18\x18"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"+\xedO\xfd\x8e[@\x87\x8bj>\xd5\xba"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x10\xee\xba\xc7\x00\xd95\x01t\x92>Ig\xa8\x001\xdb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_1.object(*var_0)
