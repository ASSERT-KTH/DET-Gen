# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1465 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "9v\r\\"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_1():
    bytes_0 = b"[Iy\xea\xc6\xe0\xa5\x98P\xf7l\xd0;"
    list_0 = [bytes_0, bytes_0, bytes_0]
    list_1 = [list_0]
    var_0 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "#}b53x>nQx>w;Wb8Gm}"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    dict_0 = {str_0: str_0, str_0: str_0}
    module_1.object(**dict_0)