# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1988 as module_0


def test_case_0():
    bool_0 = True
    str_0 = "<MI[g\x0c^wX{t#Ga\x0b"
    list_0 = [bool_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1007.529033
    set_0 = {float_0}
    list_0 = [float_0, set_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    var_1 = module_0.func(*list_0)
    list_1 = [none_type_0]
    module_0.func(*list_1)