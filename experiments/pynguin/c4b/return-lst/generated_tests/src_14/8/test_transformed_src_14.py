# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_14 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    bool_1 = False
    set_0 = {bool_1}
    tuple_0 = (bool_0, bool_0, bool_1, set_0)
    var_0 = module_0.func(*tuple_0)
#    module_0.func()
