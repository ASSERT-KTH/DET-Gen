# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1511 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x19_\xa5f\xd7"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x19_\xa5f\xd7"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 1
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = 'h*C&2"O/['
    bool_0 = True
    tuple_0 = (str_0, bool_0, bool_0)
    var_0 = module_0.func(*tuple_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = 'h*C&2"O/['
    tuple_0 = module_0.func(*str_0)
    var_0 = module_0.func(*tuple_0)
    bytes_0 = b"\x19_\xa5f\xd7"
    list_0 = [bytes_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*list_0)
    object_0 = module_1.object()
#    module_0.func()
