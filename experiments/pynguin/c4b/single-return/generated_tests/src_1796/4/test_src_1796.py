# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1796 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    none_type_0 = None
    list_1 = [none_type_0, none_type_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"WZ\x8d\x12\xd5\x1aI>\xff\x9d6e"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 245
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x04\\\x00\xe0Bn\xc6\xdaG\xe9O\xd4\x11\x95X\x18U"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x1e\xb2\xdd-\xf4\xabk\xe7F\xba\xb3\x960\xf2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 210
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"k\x0etQ\xd2Z\x0e\xf8\x01"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 49
    var_1 = module_1.object()
    module_0.func()
