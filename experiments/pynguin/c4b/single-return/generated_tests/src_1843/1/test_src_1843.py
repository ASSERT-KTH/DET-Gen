# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1843 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"r\xec\xda\x12\xe2\x16A\xb6\xca\xb7\xf3\x864Us\xefd\x82Fx"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 14
    module_0.func()


def test_case_2():
    bytes_0 = b"r\xaf\xda\x12\xe2\x16A\xb6\xca\xb7\xf3\x864Us\xefd\x82Fx"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 15
    var_1 = module_1.object()
