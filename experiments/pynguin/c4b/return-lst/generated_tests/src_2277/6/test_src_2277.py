# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2277 as module_0


def test_case_0():
    bytes_0 = b"\xd3\xc4FC\x83k\x89\xc0\xc7"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    set_0 = set()
    int_0 = 757
    list_0 = [set_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\x0cd+D^8;!b4KUO$#Q"
    list_0 = [str_0, str_0, str_0]
    list_1 = [list_0, list_0, list_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_1)
    module_0.func()
