# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_533 as module_0
import builtins as module_1


def test_case_0():
    int_0 = -1624
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    dict_0 = {object_0: object_0, object_0: object_0}
    list_0 = [dict_0, object_0]
    var_0 = module_0.func(*list_0)
    bool_0 = True
    bytes_0 = b"I9N`\xcdB\xf66|f\xe6\x87\xfc\x86\xf0\xb9"
    list_1 = [bool_0, bool_0, bool_0, bytes_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == "NO"
#    module_0.func()
