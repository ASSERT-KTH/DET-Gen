# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1045 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    set_0 = {bytes_0, bytes_0, bytes_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 4
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"8"
    set_0 = {bytes_0, bytes_0, bytes_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 3
    var_1 = module_1.object()
    module_0.func()
