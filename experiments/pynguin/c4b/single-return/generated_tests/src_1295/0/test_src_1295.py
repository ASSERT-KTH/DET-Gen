# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1295 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "*tgK)J"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "H\x0c\x0cf:hq_7meK%VKC"
    bool_0 = True
    list_0 = [bool_0]
    list_1 = [str_0, list_0, bool_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "StgK)9J"
    bool_0 = True
    list_0 = [bool_0]
    list_1 = [str_0, list_0, bool_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_1)
    assert var_1 == "YES"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = " tgFK)Q"
    bool_0 = False
    list_0 = [bool_0]
    list_1 = [str_0, list_0, bool_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
    module_0.func()
