# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2007 as module_0


def test_case_0():
    int_0 = -611
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    list_1 = [var_0, list_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == -1


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 631
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "4477777777777777777777777777777777777777777777777777777777777777777777777777777777777777777"
    )
#    module_0.func()
