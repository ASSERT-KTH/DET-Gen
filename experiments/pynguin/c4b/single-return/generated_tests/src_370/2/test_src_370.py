# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_370 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"c\x0b\xf6M\x02\x96l\xa3S2\xe7\xc2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b".a\xd5b\xd97Q?\xc5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 9
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf2\x1ci\x11\x8d"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 14
    module_1.object(*var_0, **bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"0\xe1\x95\x17\x00\xbfP\xb7\xa6\xfe\xcd\x92\xcf2\x9d\xa4"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 0
    module_0.func(*var_0)
