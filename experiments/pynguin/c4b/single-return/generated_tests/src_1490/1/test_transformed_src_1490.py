# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1490 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "C*^R=;,z4csa~NS9OVu"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "C*^P=;,z4csa~NS9OVu"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
#    module_0.func()
