# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1796 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -96.58138
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'/5\xe6"\xac\x8a\xee\x92\xe1&\x17rs\x178\xf6\xba'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 182
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b'/\xe6"\xac\x8a\xee\x92\xe1&\x17s\x178\xba'
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 56
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x9d\x86\x00\x8d\xc9\x87\xfca\xef\x98\x1c&\x12\xb1\xf0\xe4\xf1\xf7\xf0L"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    object_0 = module_1.object()
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x92\x00\xbbX\n\xb3\xc8\xa8\x04\xeb\xcdh\xf1"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x16\xd7\xbfdu\x17"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 154
    object_0 = module_1.object()
    module_1.object(*object_0, **object_0)
