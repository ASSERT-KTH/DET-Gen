# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_2446 as module_1


def test_case_0():
    object_0 = module_0.object()
    tuple_0 = (object_0, object_0)
    list_0 = [tuple_0, tuple_0]
    var_0 = module_1.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "kUd;qH1#{"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_1.func(*str_0)
    list_1 = [str_0, list_0, var_0]
    var_1 = module_1.func(*list_1)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Ds#[Df~Qq/^e"
    dict_0 = {str_0: str_0}
    list_0 = [str_0, str_0, dict_0]
    var_0 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "1oR9cW%|K"
    dict_0 = {str_0: str_0}
    list_0 = [str_0, str_0, dict_0]
    var_0 = module_1.func(*list_0)
    var_1 = module_1.func(*list_0)
    var_2 = module_1.func(*str_0)
    var_3 = module_1.func(*list_0)
    module_0.object(*var_3, **var_1)