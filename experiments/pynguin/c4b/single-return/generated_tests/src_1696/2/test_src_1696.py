# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1696 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "sD( Iat\r+\r\x0bJCHC"
    object_0 = module_1.object()
    list_0 = [object_0]
    list_1 = [str_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == "t"
    none_type_0 = None
    module_0.func(*none_type_0)
