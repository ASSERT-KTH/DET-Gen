# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2163 as module_0


def test_case_0():
    bytes_0 = b"\xd5\xcc\x0cC{"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    str_0 = '=A"f%<ZH?KF?7'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)


def test_case_3():
    str_0 = "Uit"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    bytes_0 = b"\xd5\xcf\xcc\x0cC{"
    list_1 = [list_0, list_0, bytes_0, list_0]
    var_1 = module_0.func(*list_1)
