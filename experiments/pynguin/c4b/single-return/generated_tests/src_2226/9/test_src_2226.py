# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2226 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"1\x83\xe0\xa3\xa8\x99"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"pe\xefX\xff4\xc7\x8fD'\xc0:Y\xe1\xaa\x91\x95\xe7\xe8"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    bool_0 = True
    tuple_0 = ()
    dict_0 = {bool_0: tuple_0, tuple_0: bool_0}
    module_0.func(*dict_0)
