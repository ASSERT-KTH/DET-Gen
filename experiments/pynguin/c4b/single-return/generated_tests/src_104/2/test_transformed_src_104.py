# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_104 as module_0


def test_case_0():
    bytes_0 = b"\x07L"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "aabbaab"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
