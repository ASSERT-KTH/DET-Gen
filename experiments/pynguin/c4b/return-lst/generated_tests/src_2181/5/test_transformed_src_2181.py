# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2181 as module_0
import builtins as module_1


def test_case_0():
    int_0 = 81
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    bool_0 = False
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    list_1 = [bool_0, bool_0, var_0, list_0, bool_0, var_1]
    var_3 = module_0.func(*list_1)


def test_case_1():
    int_0 = 3086
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


def test_case_3():
    int_0 = 78
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    bool_0 = True
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    bytes_0 = b"a\x8f\xb3\xd0\xfd\xf6\x83\xdad\xa3P\x0cb\xb9};\xa9\xc8\xdf"
    list_1 = [bool_0]
    var_3 = module_0.func(*list_1)
    var_4 = module_0.func(*bytes_0)


def test_case_4():
    int_0 = 99
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    bytes_0 = b'a\x8f\xb3\xd0\xfd\xf6\x83d\xa3P\x0cb\xb9}";\xa9\xc8\xdf'
    var_3 = module_0.func(*list_0)
    var_4 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 60
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    object_0 = module_1.object()
    object_1 = module_1.object()
    var_3 = module_0.func(*var_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 81
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    var_3 = module_0.func(*var_1)
    var_4 = module_0.func(*var_3)
#    module_0.func()


def test_case_7():
    int_0 = 30
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    bool_0 = True
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*var_1)
    list_1 = [bool_0]
    var_3 = module_0.func(*list_1)
    var_4 = module_1.object()