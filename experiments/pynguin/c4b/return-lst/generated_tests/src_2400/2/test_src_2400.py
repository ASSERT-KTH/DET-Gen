# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2400 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    list_1 = [list_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    list_1 = [tuple_0, tuple_0, tuple_0, tuple_0]
    var_1 = module_0.func(*list_1)
    object_0 = module_1.object()
    str_0 = "e@\\.}zN9p )I~R1!-[]~"
    var_2 = module_0.func(*str_0)
    list_2 = [object_0, object_0, str_0]
    module_0.func(*list_2)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
