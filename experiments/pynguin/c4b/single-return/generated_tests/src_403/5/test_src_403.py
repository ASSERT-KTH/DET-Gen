# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_403 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x7f{U\x86\x88\xdd\xc8ou+\x89\xb6\x8f2\xa0\xa7\xdd\xa5\xc6^"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
    module_0.func()
