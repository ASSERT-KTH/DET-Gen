# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1727 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "458UH)IY2`\x0b33"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "3a|`d?}\x0c\x0b.nFK$R"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"
#    module_0.func()
