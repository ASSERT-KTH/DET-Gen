# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1359 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\x0c\nR"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 8


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "h~\nBKi\\SnD)}b99E"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 5
    module_1.object(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "a\x0c:J|tLT_/p"
    set_0 = {str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 5
    str_1 = "wAuY^<2h|{1@`U@(f|"
    list_0 = [str_1, str_1, str_1, str_1]
    var_1 = module_0.func(*list_0)
    assert var_1 == 8
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "R1x0cGC"
    set_0 = {str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 5
    str_1 = "h~\nBKi\\SnD)}b99E"
    list_0 = [str_1, str_1, str_1, str_1]
    var_1 = module_0.func(*list_0)
    assert var_1 == 5
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "h8\nBKH\\SnD)}b{9E"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    object_0 = module_1.object()
    module_0.func()
