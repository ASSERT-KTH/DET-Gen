# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1848 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x7f\xb6\xa3\xeeN\xcdb\xb7"
    list_0 = []
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object(*list_0)
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"s\xbc\xe9\xd9|LS\xc8\xe8\xa8\x03\xfdX\x0e\xea\x92\xb2"
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object()
    object_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xf5\x8fxR\xcd\x8c\xf9n\xf4\xc7\xc9\xb7\x91^\xbe\xd4\xb9\xb9\xaa\xcf"
    list_0 = []
    var_0 = module_0.func(*bytes_0)
    object_0 = module_1.object(*list_0)
    object_1 = module_1.object()
    module_0.func(*object_1)