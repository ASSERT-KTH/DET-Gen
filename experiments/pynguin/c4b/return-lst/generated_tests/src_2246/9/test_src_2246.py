# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2246 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "5q'8nRC\\\x0c*OQr:8E"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    list_1 = [str_0, str_0, str_0, str_0]
    tuple_0 = (str_0, list_1, str_0)
    list_2 = [tuple_0]
    module_0.func(*list_2)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "W/3TZo#Ek)TXKV(/"
    int_0 = -409
    list_0 = [str_0, int_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
