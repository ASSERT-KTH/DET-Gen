# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_102 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    dict_1 = {}
    list_0 = [bool_0, dict_0, dict_1]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
