# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import wrap as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -646
    module_0.wrap(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    bool_0 = False
    var_0 = module_0.wrap(dict_0, bool_0)
    module_0.wrap(var_0, bool_0)


def test_case_2():
    str_0 = "<T.X\rU&f\n~0aoU0I\x0b\x0c\n"
    bool_0 = True
    var_0 = module_0.wrap(str_0, bool_0)