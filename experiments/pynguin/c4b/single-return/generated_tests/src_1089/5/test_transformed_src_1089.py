# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1089 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1841
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES\n0"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"_\x08eu"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "NO"
    int_0 = 1830
    list_0 = [int_0, int_0, int_0, int_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "YES\n0"
#    module_0.func()
