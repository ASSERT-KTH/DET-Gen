# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_398 as module_0


def test_case_0():
    list_0 = []
    int_0 = -885
    tuple_0 = (list_0, list_0, int_0, int_0)
    var_0 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "U>z-M^O%:,fF$*"
    list_0 = [str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xa2\x83\xfe9\\\x86\xc3\xc0k\xa8"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    bool_0 = False
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "4tr0VX:N`Cn+] Vb"
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "4tr0VX:N`Cn+] Vb"
    var_0 = module_0.func(*str_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "47crdY.m%hU@"
    list_0 = [str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = '767c"vY.%hU@'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*str_0)
    module_0.func(*list_0)
