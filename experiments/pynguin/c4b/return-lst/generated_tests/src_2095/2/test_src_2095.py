# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2095 as module_0


def test_case_0():
    bytes_0 = b"%\xeb\x89p\xe0\xde\xff\x0fv\x19\xf2\xd0"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bytes_0 = b"k"
    dict_0 = {}
    bool_0 = False
    tuple_0 = (bytes_0, bytes_0, dict_0, bool_0)
    var_0 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
