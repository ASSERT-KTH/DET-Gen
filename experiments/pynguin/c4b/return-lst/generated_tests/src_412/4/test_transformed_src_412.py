# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_412 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "#$*"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"<5C"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    list_0 = []
    str_0 = "aI"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_0)
    list_1 = [var_1, var_2, list_0, var_2]
    var_4 = module_0.func(*list_1)
    object_0 = module_1.object()
#    module_0.func()