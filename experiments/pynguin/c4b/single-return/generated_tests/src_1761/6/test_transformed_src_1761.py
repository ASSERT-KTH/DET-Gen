# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1761 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\xa5\x7f8[/\x9f<\x0e\xde\x06\xc8\xb7Y"\xb2\xf05'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -1596.833
    list_0 = [float_0, float_0]
    list_1 = [float_0, list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 0
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()