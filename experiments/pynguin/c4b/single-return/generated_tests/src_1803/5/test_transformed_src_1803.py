# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_1803 as module_1


def test_case_0():
    object_0 = module_0.object()
    list_0 = [object_0]
    var_0 = module_1.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_1.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "r/\\wTz`!h\x0b \t<=\x0bny"
    list_0 = [str_0, str_0, str_0]
    dict_0 = {str_0: list_0}
    tuple_0 = (list_0, dict_0)
    list_1 = [tuple_0, tuple_0]
    var_0 = module_1.func(*list_1)
    assert var_0 == 1
#    module_1.func()
