# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2552 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bool_1 = True
    list_0 = [bool_0, bool_0, bool_1]
    var_0 = module_0.func(*list_0)
    tuple_0 = ()
    dict_0 = {tuple_0: tuple_0}
#    module_0.func(*dict_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    int_0 = 126
    bytes_0 = b"\xe3\xe0"
    list_1 = [int_0, bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)
    var_3 = module_0.func(*list_1)
#    module_0.func()
