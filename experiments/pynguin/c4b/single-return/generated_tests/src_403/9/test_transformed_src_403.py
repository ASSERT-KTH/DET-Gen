# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_403 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xfa\xf2\xba<\x9d\x82\xc4$X'\xf0\xd46\x08\xd74\xfd\x02@"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 797.9104662616479
    list_0 = [float_0, float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    list_1 = [float_0, float_0, float_0]
    tuple_0 = (float_0, list_1)
    list_2 = [var_0, tuple_0]
#    module_0.func(*list_2)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf5\x9d\x8bi\xb4\xac\xb6\xa4\x05\x95\x85\xc7\n/\xb0\xe07"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
#    module_0.func(*var_0)
