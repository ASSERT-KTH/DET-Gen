# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2183 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -1741
    bytes_0 = b"6\xd8w\x0f\xb2'\x83\xd2\x89\xcf\xb01\xc1"
    tuple_0 = (int_0, int_0, bytes_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    module_0.func(*bytes_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x12\xb5?\xb8\x12h"
    set_0 = {bytes_0}
    float_0 = 28.163784928863357
    list_0 = [float_0, bytes_0, set_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 801.9945304802291
    bytes_0 = b'\x07"\xd0\xa96\x13\xe7\x87YriJ\x14R\x7f\xb5\xfa"'
    list_0 = [float_0, bytes_0, bytes_0, float_0]
    var_0 = module_0.func(*list_0)
    list_1 = [var_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = -1027
    list_0 = [int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    float_0 = 1.648259989972622
    bytes_0 = b'\x07\x02\xd06\x13\x87Yr\xe7(JDpR\xdd\x7f\xb5\xfa"'
    list_1 = [float_0, bytes_0, bytes_0, bytes_0, float_0]
    var_1 = module_0.func(*list_1)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = -1027
    list_0 = [int_0, int_0, int_0, int_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    float_0 = 4.782785284949423
    bytes_0 = b"\x07\x04\xd06\x13QYr\xe7(\x16DpR\xdd\x7f\xb5\xfa"
    list_1 = [float_0, bytes_0, bytes_0, bytes_0, float_0]
    var_1 = module_0.func(*list_1)
    module_1.object(**var_0)
