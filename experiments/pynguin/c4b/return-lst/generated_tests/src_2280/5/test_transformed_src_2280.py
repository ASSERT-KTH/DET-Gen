# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2280 as module_0


def test_case_0():
    int_0 = 2343
    set_0 = {int_0, int_0}
    list_0 = [set_0, int_0, set_0]
    list_1 = [int_0, int_0, list_0, int_0]
    var_0 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b'\xe9\x00\xef\xbe\xe6\t\\\xd7@y\xe5\x92\xcb"\xd4\x88?'
    var_1 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
