# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1485 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b'\t\x0cI|"\xb7>\xcd\xc3w'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'\tV\x0cI|"\xb7>\xcd\xc3w'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 22
#    module_0.func(*var_0)