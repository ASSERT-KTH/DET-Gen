# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import wrap as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    float_0 = 3166.450731167947
    set_0 = {object_0, float_0}
    var_0 = module_1.wrap(set_0, float_0)
    module_1.wrap(object_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "|Q"
    module_1.wrap(str_0, str_0)


def test_case_2():
    bool_0 = True
    str_0 = "\x0c}j=lRS?aB@0dvz+h~s_"
    var_0 = module_1.wrap(str_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "/vE "
    bool_0 = True
    var_0 = module_1.wrap(str_0, bool_0)
    module_1.wrap(str_0, var_0)