# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_325 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0}
    list_0 = [bool_0, set_0, set_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    bool_0 = False
    str_0 = "u{1Ejp;jP"
    dict_0 = {bool_0: bool_0, bool_0: str_0, str_0: bool_0}
    var_0 = module_0.func(*dict_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    str_0 = "u{i11Ejp;j"
    list_0 = [bool_0, str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*bool_0)