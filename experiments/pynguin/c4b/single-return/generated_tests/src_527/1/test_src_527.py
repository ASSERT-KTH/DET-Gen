# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_527 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"B\xc0p*]L'G\x10'%"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"B\xc0\x12\xbe*]LG\x10'%"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"B$\xf8\x11\xbe*]L';\x10'%"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 18
    module_1.object(**var_0)
