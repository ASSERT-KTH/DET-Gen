# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_479 as module_0


def test_case_0():
    bytes_0 = b"\x14\xe5t\xd0\xc23\x13\xef[\x98\x01k\xf7\\\x83\x0c\xd6\xb6"
    set_0 = {bytes_0, bytes_0}
    list_0 = [bytes_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "D>(i\n;+|+=FL,+m2ciA"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bool_0 = True
    list_1 = [bool_0, list_0, var_0, bool_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 3
#    module_0.func()
