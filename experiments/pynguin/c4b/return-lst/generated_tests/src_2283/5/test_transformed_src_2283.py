# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2283 as module_0
import builtins as module_1


def test_case_0():
    str_0 = ".'*st`=R.BGt"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    object_0 = module_1.object()
    list_0 = [object_0, object_0, object_0, object_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "r)Wh50do 0\nXi"
    bytes_0 = b"\xde\xde\xe8\xfb\x10N\xbf\x89Q"
    str_1 = "c'`p1%mC_yjn\rwlbG"
    tuple_0 = (str_0, bytes_0, str_1)
    list_0 = [tuple_0, str_1, tuple_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)
#    module_0.func()
