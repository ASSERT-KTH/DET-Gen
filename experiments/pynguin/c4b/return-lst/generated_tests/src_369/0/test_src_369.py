# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_369 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "E'\t4D84S`j|O0*|"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "E'\t4D84S`j|O0*|"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_2():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    object_0 = module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "EC*[q%s829"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
