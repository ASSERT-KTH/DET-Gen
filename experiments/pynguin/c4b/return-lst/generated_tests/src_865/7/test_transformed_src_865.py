# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_865 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "Jcm9\nXq\tUGTz\nk'"
    object_0 = module_0.func(*str_0)


def test_case_2():
    str_0 = "L@\nKee\\Hq"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "Jcm9\nXq\tUGTz\n'"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "[QZ9\x0ci/G &E3$V@)/')Q"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()