# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2219 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bytes_0 = b'\xa2opJ\xb6\xdfi\x8du&\x80"\xb7\xbc5F\x0c\xff'
    dict_0 = {bool_0: bool_0, bool_0: bytes_0}
    list_0 = [dict_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "tk`5atQU\x0cSu"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()
