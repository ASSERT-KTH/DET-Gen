# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"H_\xe8 \xd6\x7f.\xef\x8b\xa5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
    bytes_0 = b'".P_\x01ZF=U\x8c='
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 2
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"cZ6\xfd\xb4\xbbjM \xe1\x1e\x08\xf9@\x1b\x82\xb3j"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x1b=\xb9\xc4"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"+\xbf\xc2\x92\xbe\xfchq\xdc\xffn\x83\xdd\xd0\x1f\xffy"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    var_1 = module_1.object()
    var_2 = module_0.func(*bytes_0)
    assert var_2 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\x0f:\x97\x08\x1an\xf5F&%hz\x9f\x12\x1b\xbfp\x87\xa7B"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    list_0 = [var_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 1
    module_0.func()
