# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2219 as module_0


def test_case_0():
    str_0 = "ht3'XnCK&U"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "OHVAuP!_UR'~mpQ\x0b||z"
    set_0 = {str_0, str_0}
    bool_0 = True
    set_1 = set()
    list_0 = [str_0, set_0, bool_0, set_1]
    var_0 = module_0.func(*list_0)
    module_0.func()
