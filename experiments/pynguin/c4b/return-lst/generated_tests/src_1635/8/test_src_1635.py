# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1635 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xae\xe2T\x88\xf1\xe5\xb5\xa7"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
