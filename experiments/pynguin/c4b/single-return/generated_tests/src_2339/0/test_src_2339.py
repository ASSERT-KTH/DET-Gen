# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2339 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"ccLn\x18y\x91\x87"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    list_1 = [list_0, list_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'WP9(bB\n\x0bM"Q;'
    int_0 = 3526
    list_0 = [str_0, str_0, int_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "YES"
    object_0 = module_1.object()
    var_1 = module_0.func(*str_0)
    assert var_1 == "NO"
    var_2 = module_1.object()
    module_0.func()
