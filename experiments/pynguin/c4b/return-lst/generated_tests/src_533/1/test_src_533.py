# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_533 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"\xd4q\xd9\x90\x0f\x1f\xa7f"
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    object_0 = module_1.object()
    list_0 = [object_0, object_0, object_0, object_0]
    var_0 = module_0.func(*list_0)
    object_1 = module_1.object()
    object_2 = module_1.object()
