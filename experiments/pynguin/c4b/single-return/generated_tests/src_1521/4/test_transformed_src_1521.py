# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1521 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bool_0 = True
    str_0 = "bH\x0bd>\x0c"
    list_0 = [bool_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    str_0 = "P\x0cpvMAti"
    list_0 = [bool_0, str_0, str_0, bool_0]
    str_1 = "4"
    list_1 = [str_1, list_0, str_1]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1
#    module_0.func()
