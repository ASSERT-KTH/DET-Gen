# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2160 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "9b9"
    var_0 = module_0.func(*str_0)
    assert var_0 == -1
    set_0 = {str_0, str_0, str_0, str_0}
    module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b">\xd1u\xf9{\x88U@#\xac\x03\xa4\x8cw\x1a"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "939"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 21
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "90329908"
    set_0 = {str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 903307
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "9390"
    set_0 = {str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 102
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "980329208"
    set_0 = {str_0, str_0, str_0, str_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 980357
    object_0 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_7():
    bool_0 = False
    set_0 = {bool_0}
    list_0 = [set_0, set_0, set_0, set_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == -1
    str_0 = "906299908"
    set_1 = {str_0, str_0, str_0, str_0}
    var_1 = module_0.func(*set_1)
    assert var_1 == 906397
    module_0.func()
