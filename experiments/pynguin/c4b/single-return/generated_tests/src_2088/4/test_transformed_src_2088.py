# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2088 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xc5\xcd"
    list_0 = [bytes_0, bytes_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "U_%gV"
    var_0 = module_0.func(*str_0)
    assert var_0 == "."
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "3<]di\tz"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".3.<.].d.\t.z"
#    module_0.func()
