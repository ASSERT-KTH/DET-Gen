# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1453 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9b:\xa6r\x9f\xdb\xd4e\x98\xf5\xbf]\x13\x99\x0f\x15"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x7f\x9b.\x10:\xc5\x173%"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
#    module_0.func()
