# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_258 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xf3\xc7Oa4'K\xac\x12\xb8"
    var_0 = module_0.func(*bytes_0)
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xec\x07Oa4'\xac\x12"
    int_0 = 688
    var_0 = module_0.func(*bytes_0)
    module_0.func(*int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bytes_0 = b"\xf32\xc7Oa4'K\xac\x12\xb8"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
    module_0.func(*bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"Oa4'K\xac\x12\xb8"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    bytes_0 = b"-2\xc7Oa4'K\xac\x90\x12\xb8"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    module_0.func(*bool_0)
