# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2222 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = 'q;ax1#Q;OJ"u!'
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


def test_case_2():
    str_0 = 'q;ax1#Q;OJ"u!'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


def test_case_3():
    str_0 = "\\_eO{?o(E<0|8HrT*"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"


def test_case_4():
    str_0 = "!9"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"