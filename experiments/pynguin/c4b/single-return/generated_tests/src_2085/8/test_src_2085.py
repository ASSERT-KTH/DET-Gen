# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2085 as module_0


def test_case_0():
    str_0 = "{sjc50\\nb6(DITzG*s["
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "a*~t4xR94HAa"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    str_0 = "<QmyvZqC"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    var_1 = module_0.func(*str_0)
    assert var_1 == "NO"
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    var_2 = module_0.func(*dict_0)
    assert var_2 == "NO"
    var_3 = module_0.func(*var_2)
    assert var_3 == "NO"
    module_0.func()