# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2295 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
    var_1 = module_0.func(*list_0)
    assert var_1 == "CHAT WITH HER!"
    var_2 = module_0.func(*var_0)
    assert var_2 == "IGNORE HIM!"
    none_type_1 = None
    var_3 = module_0.func(*var_1)
    assert var_3 == "IGNORE HIM!"
    var_4 = module_0.func(*var_2)
    assert var_4 == "IGNORE HIM!"
    var_5 = module_0.func(*list_0)
    assert var_5 == "CHAT WITH HER!"
    list_1 = [none_type_1, none_type_1, none_type_0]
    var_6 = module_0.func(*list_1)
    assert var_6 == "CHAT WITH HER!"
    module_0.func()
