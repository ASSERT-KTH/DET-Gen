# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"1\t\xb1\x82\xdfs\xc9\xf2\x1d\xf1\x84\x0b\xd7"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
