# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_38 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xe1\xe5\xe3>\x17"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Penny"
    str_0 = '0~ lFDe;q{Mz7a6kg"0g'
    bool_0 = False
    list_0 = [str_0, bool_0, bool_0]
#    module_0.func(*list_0)
