# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_799 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    list_0 = [set_0, set_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = ""
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "4"
    set_0 = {str_0, str_0, str_0}
    list_0 = [str_0, set_0, set_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xb7C\xe0\x8a\x1f\x01\xcf.\xd1q\xe8"
    str_0 = "QI"
    list_0 = [bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "7"
    list_1 = [str_1, str_1, str_1, str_1, str_1]
    var_1 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\xb7C\xe0\x8a\x1f\x01\xcf.\xd1q\xe8"
    str_0 = "QI"
    list_0 = [bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    str_1 = "7"
    list_1 = [str_1, str_1, str_1, str_1, str_1]
    list_2 = [bytes_0, list_1]
    var_1 = module_0.func(*list_2)
    var_2 = module_0.func(*list_1)
#    module_0.func()