# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "XnrVtp7G\r.\n?dw"
    bool_0 = True
    var_0 = module_0.kth(str_0, bool_0)
    assert var_0 == "\r"
    float_0 = -648.28324
    module_0.kth(float_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe1\xd8\xf4"
    module_0.kth(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    object_0 = module_1.object()
    module_0.kth(bool_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'N0W3\x0bn#"Hs/,R|'
    bool_0 = True
    var_0 = module_0.kth(str_0, bool_0)
    assert var_0 == '"'
    module_0.kth(str_0, var_0)