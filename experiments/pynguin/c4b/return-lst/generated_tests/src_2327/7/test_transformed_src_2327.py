# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2327 as module_0


def test_case_0():
    bytes_0 = b"\xd0\x9a\xef^\xc22tP\r\x06\x9c\xb7\xbf\x05\xe8"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Q"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    bool_0 = True
    list_0 = [dict_0, bool_0, str_0]
    list_1 = [list_0, list_0, list_0, bool_0, str_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*var_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "6.Ic';ro>C<HD8\t"
    str_1 = ":grme) A)-Xnm"
    list_0 = [str_0, str_0, str_1]
    var_0 = module_0.func(*list_0)
    str_2 = "Q"
    bool_0 = True
    list_1 = [bool_0, bool_0, str_2]
    list_2 = [list_1, list_1, list_1, bool_0, str_2]
    var_1 = module_0.func(*list_2)
    var_2 = module_0.func(*var_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "9"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    bool_0 = True
    list_0 = [dict_0, bool_0, str_0]
    list_1 = module_0.func(*str_0)
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)
    var_3 = module_0.func(*var_2)
#    module_0.func()
