# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_177 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    complex_0 = 1074.963947 + 1809.903j
    dict_0 = {complex_0: complex_0, complex_0: complex_0}
    list_0 = [dict_0, dict_0, dict_0, complex_0, dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "@eN:}NJ5(an.LG5k"
    bytes_0 = b"T\xf5\xc68\x12\x926N\x18\xe2\xedF0\xfaA\x00"
    tuple_0 = (str_0, bytes_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == 17
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "nU"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    tuple_0 = (str_0,)
    var_1 = module_0.func(*tuple_0)
    assert var_1 == 2
    module_0.func(*var_1)
