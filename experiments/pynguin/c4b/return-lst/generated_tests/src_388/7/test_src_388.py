# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_388 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb8\xdc\x00Y\x11~\\#\xa4\xb4v\x15\x17\xf6\xb9\xec\x82"
    tuple_0 = (bytes_0,)
    list_0 = [tuple_0, tuple_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "W\t@v+f{gVET8,"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
