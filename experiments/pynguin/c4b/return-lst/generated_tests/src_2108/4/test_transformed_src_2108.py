# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2108 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xa2\xc5\xfd/,"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    bool_0 = True
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xc5\x9c$\xec/\xf5,"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa2\x85\xfdo,"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*bytes_0)
    list_1 = [bool_0, bool_0, bool_0, bool_0]
    var_3 = module_0.func(*list_1)
#    module_0.func()
