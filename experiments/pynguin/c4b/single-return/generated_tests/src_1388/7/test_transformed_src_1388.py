# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1388 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -2638.5798
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1759
    bytes_0 = b"\n\xefL\xa8\xde\xb6\xe1\xdb\xd8\xe2$\x01\x8dP\x0b\xa7_\x02\xfc\x8c"
    list_1 = [var_0, bytes_0, var_0, float_0]
    list_2 = [list_1, var_0, list_0]
#    module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1188
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 792
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
