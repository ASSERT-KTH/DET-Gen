# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_212 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "3k2"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    bytes_0 = b""
    bytes_1 = b"~[+\x06\xd7\rO\x82"
    tuple_0 = (var_0, bytes_0, bytes_1)
    set_0 = {tuple_0}
    module_1.object(**set_0)
