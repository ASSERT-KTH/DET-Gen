# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_833 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\\\x17\xf6\x95\x08\xab\x9d;\xdd\xac\xb6\xe3\xef"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf6\x95\x08\x9d\x03;\xdd\xac\xb6\xe3\xef"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"{t\xc7lz\xbd"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
