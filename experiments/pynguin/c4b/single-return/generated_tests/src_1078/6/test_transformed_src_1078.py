# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1078 as module_0


def test_case_0():
    bytes_0 = b'\x08\x13\xb4\x07\xf0"\xc17\xd8Z].\xf2\xe0\xc0\xf4\x83'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 71


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
