# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2219 as module_0


def test_case_0():
    set_0 = set()
    bool_0 = True
    list_0 = [set_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Bqw/9nO.i\x0bx1KB{mrgH"
    list_0 = [str_0, str_0]
    int_0 = 2828
    dict_0 = {}
    var_0 = module_0.func(*list_0)
    list_1 = [list_0, int_0, dict_0, dict_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*str_0)
    module_0.func()
