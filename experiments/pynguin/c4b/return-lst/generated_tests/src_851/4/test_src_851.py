# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_851 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xba\x8c\xa7\x1c"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"/"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "a@AfB\nOQvOxA"
    var_0 = module_0.func(*str_0)
    module_0.func()


def test_case_4():
    bytes_0 = b"\xe2\xbb\xcbV\xf6\x99\x88UO\x1aV\xcf\xaf\xe6\x8f"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    list_1 = [bytes_0, bytes_0]
    var_1 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "T']+3^X1z'"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"s\x87B"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    module_1.object(*var_1, **list_0)
