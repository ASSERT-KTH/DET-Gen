# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2215 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"-\xc9\xa0\x84\x9f\xf1"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    float_0 = 533.1
    tuple_0 = (bool_0, bool_0, float_0)
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    module_0.func(*var_1)
