# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1495 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x91\xaf5\x8dm\xc9\x96\xb1p\xa8\x98\x8d\xcf\x0b\xbe"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"\x91\xaf5\x8dm\xc9\x96\xb1p\xa8\x98\x8d\xcf\x0b\xbe"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe74B\xc6"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == b"\xe74b\xc6"
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x86"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
