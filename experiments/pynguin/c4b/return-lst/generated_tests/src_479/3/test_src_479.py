# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_479 as module_0


def test_case_0():
    str_0 = "$-1?#\\pyE)iW_xdU%Dz"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "pZ\nSvDnfz}"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0, list_0, list_0]
    var_1 = module_0.func(*list_1)
    str_1 = "emo}m "
    var_2 = module_0.func(*str_1)
    module_0.func()
