# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_121 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    object_0 = module_0.object()
    list_0 = [bool_0, object_0]
    var_0 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_1.func(*list_0)
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"W\x00\xd0\xf6\xeb\xea\xc6\xc3p"
    var_0 = module_1.func(*bytes_0)
    module_1.func()
