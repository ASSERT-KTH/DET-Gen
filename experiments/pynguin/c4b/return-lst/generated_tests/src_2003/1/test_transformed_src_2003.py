# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2003 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"V\xfb\x8fK\xf9\x92\x82\x1b\xff\x03%c\xa5n\xcd{\x1f\x05"
    var_0 = module_0.func(*bytes_0)


def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x1cG\xccm\xe9\x8f\xd8T\xf1^\xa4tf\xdf6\x9c\xac"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 105
    dict_0 = {int_0: int_0}
    var_0 = module_0.func(*dict_0)
    bytes_0 = b"j\x1e\xb8\xf5\x08\xb5\xd7\xdb\xcf\x17\xb8i\xaa]\xc7\x14\xd6%\x14"
    var_1 = module_0.func(*bytes_0)
    float_0 = -1719.43
    object_0 = module_1.object()
    bool_0 = True
    list_0 = [float_0, float_0, float_0, bool_0]
    var_2 = module_0.func(*list_0)
#    module_0.func()
