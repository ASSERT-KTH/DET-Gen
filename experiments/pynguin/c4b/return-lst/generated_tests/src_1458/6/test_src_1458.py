# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_1458 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    object_0 = module_0.object(*dict_0)
    var_0 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_1.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "i^\x0bFEZ9"
    var_0 = module_1.func(*str_0)
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    var_1 = module_1.func(*list_0)
    var_2 = module_1.func(*list_0)
    module_1.func()
