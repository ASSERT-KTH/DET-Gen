# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2210 as module_0


def test_case_0():
    str_0 = "d"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    module_0.func(*bool_0)


def test_case_2():
    str_0 = "4ZHLS+qf3HGA#9:@q2R"
    var_0 = module_0.func(*str_0)
    assert var_0 == "NO"


def test_case_3():
    str_0 = ""
    list_0 = [str_0, str_0, str_0, str_0]
    list_1 = [list_0, str_0, str_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "YES"
