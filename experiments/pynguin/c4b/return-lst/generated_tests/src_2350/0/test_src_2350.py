# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2350 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"T\x81\x1dv\xf0\xcb\xc8\x86"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "I4\\|bzpQQy8$dq4J!8"
    object_0 = module_1.object()
    list_0 = [str_0, str_0, object_0]
    var_0 = module_0.func(*list_0)
    list_1 = [str_0, str_0]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
