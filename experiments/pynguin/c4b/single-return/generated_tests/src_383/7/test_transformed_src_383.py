# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_383 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xee5T\x94\xb5\x8e\xb2\xd3}\x0f\xc4E=`\xc8\xec"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -2127.0
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func()
