# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1796 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"[\xaf\xf0\x90\xd9\r\xc5rM\x8c\xd1*\xbbs\\\xb3"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 420


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    list_1 = []
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x0cg5\xe6\xf7c\x80\xa5\xa8\xdb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 84
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    int_0 = -2116
    list_0 = [bool_0, int_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bytes_0 = b"\x9f\x02\x06\xe2y\xb8"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 7
    var_2 = module_0.func(*list_0)
    assert var_2 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = True
    int_0 = 1985
    list_0 = [bool_0, int_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bytes_0 = b"E\x9a\xfd\xda\xb3\xea\x04\xde\x08\xb7"
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 441
    module_0.func(*var_1)
