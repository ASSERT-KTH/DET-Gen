# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "h-\\1x"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    module_0.kth(object_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 860.192
    list_0 = [float_0, float_0, float_0, float_0]
    module_0.kth(list_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x17"
    bool_0 = False
    var_0 = module_0.kth(bytes_0, bool_0)
    assert var_0 == 23
    set_0 = {bytes_0}
    module_0.kth(set_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -648.069
    list_0 = [float_0, float_0]
    module_0.kth(list_0, float_0)
