# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_32 as module_0


def test_case_0():
    bytes_0 = b"@6\x890\xe8\xd0\xdb\x7f0p\x05\xec"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 12


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    int_0 = -354
    tuple_0 = (int_0, int_0)
    list_0 = [tuple_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    bytes_0 = b"\xa7\xd21\x15\x9c"
    list_1 = [bytes_0, bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 5
