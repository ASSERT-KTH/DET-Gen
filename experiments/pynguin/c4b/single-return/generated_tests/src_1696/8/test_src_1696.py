# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1696 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcc\xaf)\x8dv"
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 204
    module_0.func()
