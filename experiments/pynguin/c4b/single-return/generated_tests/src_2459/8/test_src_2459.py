# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2459 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb2m\x1c\x91\xfe\x9a\x91>+\x15\xc8WS\xe66\x0e"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 13
    none_type_0 = None
    module_0.func(*none_type_0)
