# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2415 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"~\xe6e\xb7\xa5\x8e\xed\x0e\x8b\xc8\xcb<gV\xb9"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
