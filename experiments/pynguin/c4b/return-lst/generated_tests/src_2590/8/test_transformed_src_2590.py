# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2590 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_3():
    int_0 = -963
    object_0 = module_1.object()
    list_0 = [int_0, object_0, object_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"X\x931%\xf1\x82\xc2|\x8d\xee+sOc\xba\xa4"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()
