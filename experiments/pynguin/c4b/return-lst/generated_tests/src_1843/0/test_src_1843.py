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
    bytes_0 = b"*`4\xee\x97\xd9\x9cE#\xa3\x06\x92\x19g\xd5]"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"`4\xee\x97\xd9\x9cE#\xa3\x06\x92\x19g\xd5"
    var_0 = module_0.func(*bytes_0)
    module_1.object(*var_0)