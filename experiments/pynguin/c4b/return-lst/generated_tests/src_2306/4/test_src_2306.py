# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2306 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"_\xd4\xcc\xa5\xa1\xc3\x1bm\xb2\xe9"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
    list_0 = [bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x136k+\xe2&)\xd1\xe0N\x88\xcf"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xdc\xe9\xa4\xeb\xa5P\xf2!M6}"
    var_0 = module_0.func(*bytes_0)
    module_0.func()
