# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1264 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xed\xef\x14IL|\x1ez\xe2M\xf3n\xc6\xe3!z\x9c?\x7f\x18"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()
