# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2369 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "helT"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = "\\"
    var_0 = module_0.func(*str_0)


def test_case_3():
    str_0 = "helTPloz"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    tuple_0 = (str_0,)
    var_1 = module_0.func(*tuple_0)
    object_0 = module_1.object()
