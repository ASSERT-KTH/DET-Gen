# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2160 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "95973010"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    object_0 = module_1.object()
    object_1 = module_1.object()
    object_2 = module_1.object()


def test_case_2():
    str_0 = "95973010"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "959732010"
    var_0 = module_0.func(*str_0)
    list_0 = [str_0]
    var_1 = module_0.func(*str_0)
    var_2 = module_0.func(*list_0)
#    module_0.func()
