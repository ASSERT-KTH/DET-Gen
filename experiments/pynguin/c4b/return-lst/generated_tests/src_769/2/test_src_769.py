# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_769 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"k\xa1\xd9\xb1\xc1\x98"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
