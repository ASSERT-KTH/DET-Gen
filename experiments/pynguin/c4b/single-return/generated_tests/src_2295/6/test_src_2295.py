# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2295 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "CHAT WITH HER!"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "g\x0cl~y)*d\t\\\\aEEw2b"
    bool_0 = True
    dict_0 = {str_0: str_0, str_0: bool_0}
    list_0 = [dict_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "IGNORE HIM!"
    var_1 = module_0.func(*list_0)
    assert var_1 == "IGNORE HIM!"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
