# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1375 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 988.0
    dict_0 = {float_0: float_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == "Penny"
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    str_0 = "C<b"
    tuple_0 = (bool_0, str_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "Sheldon"
    module_0.func()