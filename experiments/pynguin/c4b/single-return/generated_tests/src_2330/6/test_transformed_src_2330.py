# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2330 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0}
    list_0 = [set_0, set_0, set_0]
#    module_0.func(*list_0)


def test_case_1():
    str_0 = "c!Dq**@@rD[@;/3c:I"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "c!Dq**@@rD[@;/3c:I"


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Yof?z^&Pf}~d@1r`"
    var_0 = module_0.func(*str_0)
    assert var_0 == "y"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0]
    bytes_0 = b""
    tuple_0 = (list_0, bytes_0, bytes_0)
    list_1 = [tuple_0, bytes_0, bytes_0, bool_0]
    var_0 = module_0.func(*list_1)
    str_0 = "kF:z9LM"
    var_1 = module_0.func(*str_0)
    assert var_1 == "K"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    list_0 = []
    bytes_0 = b""
    tuple_0 = (list_0, bytes_0, bytes_0)
    list_1 = [tuple_0, bytes_0, bytes_0, list_0, list_0, bytes_0]
    var_0 = module_0.func(*list_1)
#    module_0.func(*tuple_0)


#@pytest.mark.xfail(strict=True)
def test_case_6():
    bool_0 = False
    list_0 = [bool_0]
    bytes_0 = b"A\xe6"
    tuple_0 = (list_0, bytes_0, bytes_0)
    list_1 = [tuple_0, bytes_0, bytes_0, bool_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "\tANF"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\tANF"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "\tANF"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "\tANF"
    var_1 = module_1.object()
    list_1 = [list_0, str_0, str_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "eANF"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Eanf"
    var_1 = module_1.object()
#    module_0.func(*var_1)
