# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "genC\x0bB_if5aJ`"
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "Z"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    dict_0 = {}
    var_0 = module_0.shunting_yard(dict_0)
    str_0 = "\tjI_.\x0c#9hNd|s1"
    module_0.shunting_yard(str_0)


def test_case_3():
    int_0 = -522
    list_0 = [int_0]
    tuple_0 = (list_0, int_0)
    var_0 = module_0.shunting_yard(tuple_0)


def test_case_4():
    str_0 = "/+"
    var_0 = module_0.shunting_yard(str_0)


def test_case_5():
    str_0 = "-/+"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x91\xe7"
    var_0 = module_0.shunting_yard(bytes_0)
    var_1 = module_0.shunting_yard(bytes_0)
    bool_0 = True
    str_0 = "-/"
    var_2 = module_0.shunting_yard(str_0)
    var_3 = module_0.shunting_yard(str_0)
    bytes_1 = b"J\xca%\x9e\x9f\x96\x1f}\x07\x8d\xa0\x82\xad\x97r\x8f]"
    var_4 = module_0.shunting_yard(bytes_1)
    module_0.shunting_yard(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    bytes_0 = b"\n\xe7"
    var_0 = module_0.shunting_yard(bytes_0)
    var_1 = module_0.shunting_yard(bytes_0)
    var_2 = module_0.shunting_yard(bytes_0)
    bool_0 = True
    str_0 = "-//+"
    var_3 = module_0.shunting_yard(str_0)
    module_0.shunting_yard(bool_0)