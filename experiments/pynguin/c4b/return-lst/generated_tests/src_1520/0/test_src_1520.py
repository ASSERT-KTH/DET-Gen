# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1520 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"3b\xb1\xc0\x9c\xfc\x90\xee"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"3b\xb1\xf5\xc0\xfc\x90\xee"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"3b\xc1\xb1\xc0\x9c\xfc\x90\xee"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
    module_0.func()
