# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2113 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x0b\xf5\xee\xc0\x06\xb6Cx\x9c1\x14\xbf"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xf5\xee\xc0\x06\xb6Cx\x9c\xef\x14\xbf"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 30
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf5Y\xc0\x06\xb6x\x9c1\x14\xbf"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 32
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xee\xc0\x06\xb6Cx\x9c1\x14\xbf\x9b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 11
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b")R\xe5,\x92\xaf"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6
    bytes_1 = b"\xf5\xee\xc0\x06\xb6Cx\x9c\xef\x14\xbf"
    var_1 = module_0.func(*bytes_1)
    assert var_1 == 30
    object_0 = module_1.object()
    module_1.object(**var_1)