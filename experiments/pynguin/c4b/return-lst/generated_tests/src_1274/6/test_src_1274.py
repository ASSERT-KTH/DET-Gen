# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1274 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\x17\xff\xa2zhu5hc"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    str_0 = "|OLXZ(0|H*947n74"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_1.object()
    object_0 = module_1.object()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "|OLX@40|H7o84*'47n74"
    list_0 = [str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_1.object(*list_0)
