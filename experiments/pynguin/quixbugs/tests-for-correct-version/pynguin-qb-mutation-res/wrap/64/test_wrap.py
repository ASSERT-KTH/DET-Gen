# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0
import builtins as module_1


def test_case_0():
    bool_0 = True
    str_0 = "/\r`KDy#R`,+HohO4"
    var_0 = module_0.wrap(str_0, bool_0)


def test_case_1():
    bool_0 = False
    object_0 = module_1.object()
    dict_0 = {}
    var_0 = module_0.wrap(dict_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.wrap(bool_0, bool_0)