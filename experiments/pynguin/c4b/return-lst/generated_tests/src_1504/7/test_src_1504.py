# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1504 as module_0


def test_case_0():
    str_0 = "O7Bj;44Nk`4l44_,9"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "107B,];/DNk`4l44o_A9"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "O7B1;44N4`}4l44_,9"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    var_2 = module_0.func(*str_0)
    var_3 = module_0.func(*var_0)
    var_4 = module_0.func(*str_0)
    module_0.func()