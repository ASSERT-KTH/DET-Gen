# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    module_0.wrap(set_0, bool_0)


def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    var_0 = module_0.wrap(set_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.wrap(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "]t\t)(-X*"
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)
    none_type_0 = None
    module_0.wrap(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 2792
    str_0 = "s[R6=~({eJ*aTk1< "
    tuple_0 = (int_0, int_0, str_0, str_0)
    var_0 = module_0.wrap(tuple_0, int_0)
    int_1 = -2745
    bool_0 = True
    var_1 = module_0.wrap(str_0, bool_0)
    module_0.wrap(var_1, int_1)