# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import src_1801 as module_0
import builtins as module_1


def test_case_0():
    str_0 = ",x#B"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0


def test_case_1():
    str_0 = "B!BBnBBBi#BxB"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8
    var_1 = module_1.object()