# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xcb\x8b\x89\x08}\x93x\x0c\x95\x9a\xaf\x8b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 15
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xcb\x8b\x89\x08}\x93x\x0c\x95\x9a\xaf\x8b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 15
    object_0 = module_1.object()
    bytes_1 = b"\xd0v\xd4\x93\xe7\x13_\xf1\xf6\x99\xd3\xb0^\x87\xc5(Ff\x87"
    var_1 = module_0.func(*bytes_1)
    assert var_1 == 4
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xcb\x8b\xbb\x08\xa0\x93x\x0c4\x95\x9a\xaf\x8b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 21
    module_0.func()
