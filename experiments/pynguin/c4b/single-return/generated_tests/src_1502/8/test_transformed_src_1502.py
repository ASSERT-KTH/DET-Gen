# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1502 as module_0
import builtins as module_1


def test_case_0():
    bool_0 = False
    bool_1 = False
    set_0 = {bool_0, bool_1}
    var_0 = module_0.func(*set_0)
    assert var_0 == "0 0"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == "0 1"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -1629.1543
    str_0 = 'DZ!+8P09Z"<Cch\r}Rd'
    bool_0 = False
    tuple_0 = (str_0, bool_0)
    set_0 = {str_0}
    set_1 = {str_0}
    tuple_1 = (tuple_0, bool_0, set_0, set_1)
    tuple_2 = (float_0, tuple_1)
    var_0 = module_0.func(*tuple_2)
    assert var_0 == "-464 -462"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x8b\x9e\xe1\x07\x9en\xc0\x1a\x14\x80\x02\xfcqe\x9e\x82\x07"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "39 40"
    bool_0 = False
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    assert var_1 == "0 2"
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_2 = module_0.func(*list_0)
    assert var_2 == "0 0"
#    module_0.func()
