# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2596 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = 875
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "71111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    )
    none_type_0 = None
    list_1 = [none_type_0, none_type_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1124
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
