# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1177 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"x0v\x88\x9a"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "111111111111111111111111111111111111111111111111111111111111"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'-\xdd\x90\xae,\x16\x03o,\xf9\xb4\x84\xb1\x81"\xda\x06\xa9'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "7111111111111111111111"
    module_1.object(**var_0)
