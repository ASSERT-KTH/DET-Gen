# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1895 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xaa\xcfE\x7f\x90\xea\x04"
    set_0 = {bytes_0, bytes_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 127
    tuple_0 = (var_0,)
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xaa\xcfE\x7f\x90\xea\x04"
    set_0 = {bytes_0}
    tuple_0 = (set_0,)
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -1205.74
    bool_0 = False
    dict_0 = {bool_0: float_0}
    tuple_0 = (float_0, bool_0, dict_0)
    str_0 = "E\\.Qv*"
    list_0 = [tuple_0, tuple_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = -1205.74
    bool_0 = True
    dict_0 = {bool_0: float_0}
    tuple_0 = (float_0, bool_0, dict_0)
    str_0 = "E\\.Qv*"
    list_0 = [tuple_0, tuple_0, str_0]
    module_0.func(*list_0)
