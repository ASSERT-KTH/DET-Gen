# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2088 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    module_0.func(*bool_0)


def test_case_1():
    str_0 = "i"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "."


def test_case_2():
    str_0 = "i"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "."
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "TDQMZq`\x0cUQ0h"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".t.d.q.m.z.q.`.\x0c.q.0.h"
    bool_0 = False
    list_1 = [bool_0, bool_0, bool_0]
    module_0.func(*list_1)
