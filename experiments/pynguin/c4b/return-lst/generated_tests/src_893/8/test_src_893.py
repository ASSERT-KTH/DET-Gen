# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_893 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x07\xf7/\xc9\x85\x04\xb6\x07\x14D\x96j\xbc\x05\xf3\xc3e"
    set_0 = {bytes_0, bytes_0}
    var_0 = module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x07\xf7\xc0\xc9\x07\x04\xfc\x07\x14D\x96j\xbc\x05\xc3e"
    set_0 = {bytes_0}
    var_0 = module_0.func(*set_0)
    module_1.object(*var_0, **var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x07\xf7\xc0\xc9\x04\x07\x04\x04\x07\x14\xc5\x04\xde\x96j\x05\xc3e"
    set_0 = {bytes_0}
    var_0 = module_0.func(*set_0)
    module_0.func(*var_0)
