# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2113 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd9U# b\xa0bs{6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"XU\xbc b\xa0bs{6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    module_0.func(*var_0)
