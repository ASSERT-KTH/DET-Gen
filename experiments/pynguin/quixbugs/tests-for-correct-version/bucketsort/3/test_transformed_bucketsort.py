# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0}
#    module_0.bucketsort(set_0, bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
#    module_0.bucketsort(none_type_0, none_type_0)


def test_case_2():
    bool_0 = False
    set_0 = set()
    var_0 = module_0.bucketsort(set_0, bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    bool_0 = True
    var_0 = module_0.bucketsort(set_0, bool_0)
#    module_1.object(**var_0)
