# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xb1\xc5\xdb\xd7\x9a~\xfaw\xeedxs\x07^\xd6\x92"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xb6\xdb\x01dK\x85\xcc\xd5j\xf9\x00\xbe\xc5\x9a\xb4\xb5&\x86\x19"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 75
    bool_0 = True
    module_1.object(**bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xb1\xc5\xdb\xd7\xd0\x9a~\xfaw\xeedxs\x07^\xd6\x92"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"Z\xc4\x9c5\xd08\xec\xa6\x993\n\x8c\xec\xfa\x1a\x81t:\xa8\x95"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    module_0.func()