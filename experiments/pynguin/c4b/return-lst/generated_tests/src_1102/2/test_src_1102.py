# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1102 as module_0


def test_case_0():
    int_0 = 3039
    int_1 = 740
    tuple_0 = (int_0, int_1, int_0)
    list_0 = [tuple_0, int_0, tuple_0, int_1]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'Gu(u"I3u'
    list_0 = [str_0, str_0]
    list_1 = [str_0, str_0, list_0, str_0]
    var_0 = module_0.func(*list_1)
    module_0.func()
