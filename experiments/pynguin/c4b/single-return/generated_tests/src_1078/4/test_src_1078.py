# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1078 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcd\xe5\xb4\xc6\x94)\x9a-"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xcd\x02\xb4\xc6\x94\xbe\x9a-"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 74
    module_1.object(**var_0)
