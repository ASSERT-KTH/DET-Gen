# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2045 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "8 1"
    bool_0 = True
    list_0 = [str_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "8 93"
    bool_0 = True
    list_0 = [str_0, bool_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_1.object(*var_0)
