# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1671 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1151.445113
    list_0 = [float_0, float_0, float_0, float_0]
    list_1 = [list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"=\xf2$\x95\xc8l\x0c\xeehG}\xe1\xe1F\xa8\x0esoE\x93"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    list_0 = [dict_0, bytes_0, dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "L\n_\r(br!\n$"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
