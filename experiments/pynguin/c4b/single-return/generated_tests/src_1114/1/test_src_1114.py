# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1114 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "G<"
    object_0 = module_1.object()
    list_0 = [str_0, object_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "g<"
    module_0.func()


def test_case_3():
    str_0 = "E$SZ4u"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "E$SZ4u"


def test_case_4():
    str_0 = "E$SZ4u"
    var_0 = module_0.func(*str_0)
    assert var_0 == "e"
    list_0 = [str_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "E$SZ4u"


def test_case_5():
    str_0 = "m3`&G"
    var_0 = module_0.func(*str_0)
    assert var_0 == "M"
    list_0 = [str_0, var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "M3`&g"
