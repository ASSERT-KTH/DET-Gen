# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_102 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1056
    list_0 = [int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x91\n8y\xf0fU/\xb0\x1f\x05\xcf\xe9u]5m1\xe8"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func()
