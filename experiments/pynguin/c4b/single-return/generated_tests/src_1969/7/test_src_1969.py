# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1969 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"J\x1b\xd7e\x86s\xa1"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x1b\xd7es\xa1"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    module_0.func()
