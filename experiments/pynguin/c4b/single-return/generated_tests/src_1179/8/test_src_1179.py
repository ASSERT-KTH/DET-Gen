# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1179 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xab\xe2/\xe4g8\xb3\xc4 \xba}"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xab/\xe4g8\xb3\xc4 \xeb:\xba}"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xb604\xd9'\x9e\xd4V\x80\xe3\xcfN\x1e\x89V\x19&"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    object_0 = module_1.object()
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"p0\x9d\x9b\xdf\xe7+v\x198\x13]\x91O"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
    none_type_0 = None
    list_0 = [none_type_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"3a\xfe\xf5tG\xbd-\xf9\xbf\\v\xdb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()
