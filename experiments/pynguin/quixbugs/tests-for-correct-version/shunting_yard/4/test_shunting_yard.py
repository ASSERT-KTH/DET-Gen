# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "T-+C)tADW&gB\\/"
    module_0.shunting_yard(str_0)


def test_case_1():
    dict_0 = {}
    var_0 = module_0.shunting_yard(dict_0)


def test_case_2():
    str_0 = ","
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    module_0.shunting_yard(bool_0)


def test_case_4():
    bytes_0 = b"9\xd0 \xfeP\x9f\x9d4\x05\nA_\xe0\xcbb\x1a\xca"
    object_0 = module_1.object()
    var_0 = module_0.shunting_yard(bytes_0)


def test_case_5():
    str_0 = "/*"
    var_0 = module_0.shunting_yard(str_0)


def test_case_6():
    str_0 = "/-/"
    var_0 = module_0.shunting_yard(str_0)


def test_case_7():
    str_0 = "/-//"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "+/-//"
    var_0 = module_0.shunting_yard(str_0)
    module_1.object(**var_0)
