# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1453 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x08j\x1e\xc9Kl\xfc\x05"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 11
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x95;\xbf\xfdeu\xae\x8a\xba\xe4{\x1a\xe9\xa4\xd9\x93\xe8\xfd\n"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xc1\x0co\xa1\xfa\x94"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 24
    module_0.func(*var_0)
