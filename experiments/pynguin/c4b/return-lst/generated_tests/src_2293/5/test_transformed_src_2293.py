# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2293 as module_0


def test_case_0():
    str_0 = "\r5q,"
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = ':XZ!"b/i(Mh"l\x0ckF'
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "l<t(MheXl\nlFo"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "l<t(MheXl\nlFoD"
    list_0 = [
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
        str_0,
    ]
    var_0 = module_0.func(*list_0)
