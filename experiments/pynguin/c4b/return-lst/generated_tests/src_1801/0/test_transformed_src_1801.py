# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1801 as module_0


def test_case_0():
    str_0 = '"AGm$Di'
    var_0 = module_0.func(*str_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "[WckIOrBQBBBBBeBB"
    set_0 = {str_0}
    tuple_0 = ()
    tuple_1 = (str_0, set_0, tuple_0)
    list_0 = [str_0, tuple_1, tuple_1, tuple_1]
    var_0 = module_0.func(*list_0)
#    module_0.func()
