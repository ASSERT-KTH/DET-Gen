# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1635 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x93|\xb7\x9a\x9b%\x18/W\xa9\x8b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 356811923176489970264571492362373784095686654
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()
