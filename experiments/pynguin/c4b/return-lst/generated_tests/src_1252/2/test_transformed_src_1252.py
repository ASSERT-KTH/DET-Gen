# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1252 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0]
    str_0 = "0(\\n+W"
    tuple_0 = (bool_0, list_0, str_0)
    var_0 = module_0.func(*tuple_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()