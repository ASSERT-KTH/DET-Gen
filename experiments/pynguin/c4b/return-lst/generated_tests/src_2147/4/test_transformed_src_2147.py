# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2147 as module_0


def test_case_0():
    int_0 = -1432
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x14=\xf5\x9f\xc2\x9a\xb7\xe6\x02\x12!\xb4\x12\x13\xf2\xc5\n\x1d\x01"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.func(*dict_0)
    list_0 = [var_0, bool_0, dict_0]
#    module_0.func(*list_0)


def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    int_0 = -1432
    list_1 = [int_0, int_0]
    var_1 = module_0.func(*list_1)