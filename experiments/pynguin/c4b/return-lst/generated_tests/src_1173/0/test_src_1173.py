# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1173 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\r"
    var_0 = module_0.func(*bytes_0)


def test_case_1():
    bytes_0 = b"\r"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


def test_case_3():
    bytes_0 = b"\x1c"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x149E\xcf=\x85"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*bytes_0)
    var_2 = module_0.func(*var_1)
    object_0 = module_1.object()
    module_0.func()
