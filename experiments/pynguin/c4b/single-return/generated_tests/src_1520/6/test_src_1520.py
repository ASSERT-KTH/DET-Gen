# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1520 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcf-0\xc0\xfa\xbb\xe8\xd6\xaf\xcd\xc3\x08%\xe7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 11
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xcf-\xce\xc0\xfa\xbb\xe82\xafu\xc3\x08%\xe7\xad"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 8
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 8
    module_1.object(*var_0)
