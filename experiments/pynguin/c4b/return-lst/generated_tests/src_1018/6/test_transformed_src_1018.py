# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1018 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "8y2t?|LMN-PM"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "8y2t?|LMN-PM"
    str_1 = "\x0c{"
    list_0 = [str_1, str_0, str_1, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '53f./EsL\toh"-`Fnc'
    bytes_0 = b'\xaf\\U\xb2D\x00~\xeb\xbb\x99a\x8cw5\xb3"\x93\xa6%'
    list_0 = [str_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "530"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, var_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()
