# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_553 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'"u;\xf7\xd4\x88[\x101\rY{2\xac\xd2Qr\x00'
    set_0 = {bytes_0, bytes_0, bytes_0}
    list_0 = [set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xc9\x0b\xc3\x89\xe5\x1a\xc1\xac\x90\xb0\x0ek\x81W\x95\xbaU\xccX\xbe"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 21
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    list_1 = [tuple_0, tuple_0, list_0, tuple_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "qYzW4iv=oOuedp"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == 2
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    assert var_1 == 8
    var_2 = module_0.func(*list_0)
    assert var_2 == 8
    module_0.func()
