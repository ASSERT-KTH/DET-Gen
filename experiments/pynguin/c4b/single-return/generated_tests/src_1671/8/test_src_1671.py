# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1671 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -76
    str_0 = "1O;PisEieB]Dl6z"
    tuple_0 = (int_0, str_0, str_0, int_0)
    list_0 = [tuple_0, tuple_0, int_0, int_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "<<=5zgE\nm_G\r-hgN+"
    dict_0 = {str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 4
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
