# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2326 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Y?j@j>=3yZdXM<f;1"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    list_0 = [tuple_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Y?j@j>m=3yZdXM<f;1"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_0.func(*str_0)
    var_1 = module_1.object()
    list_1 = [object_0, object_0, object_0]
    var_2 = module_0.func(*list_1)
    module_0.func()
