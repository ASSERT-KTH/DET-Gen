# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_529 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "GEqN#eY-Rn\n"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, bytes_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, bytes_0, bytes_0, list_0, var_0, bytes_0, list_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_1.object()
#    module_1.object(**var_2)
