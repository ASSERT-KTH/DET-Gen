# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2458 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xc2e\x0cBg::\xb4:f\xb7b\xe3\x7f\xbc\xaa\xdd"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 10
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"!\xc2e\x0cBgU::\xb4:f\xb7\t\xe3\x7f\xbc\xdd"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    module_0.func(*var_0)
