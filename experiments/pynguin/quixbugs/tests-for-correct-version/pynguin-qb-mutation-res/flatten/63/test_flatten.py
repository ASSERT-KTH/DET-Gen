# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import flatten as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"n\xe7\xa0\xc3\x01T\xd5T\xc0\x06\xfa\x83\x96"
    var_0 = module_0.flatten(bytes_0)
    module_1.object(*var_0)


def test_case_1():
    object_0 = module_1.object()
    var_0 = module_0.flatten(object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"n\x9e\xa0\xc3\x01K\xd5T\xc0\x06\xfa\xfa\x96"
    list_0 = [bytes_0, bytes_0, bytes_0]
    tuple_0 = (list_0,)
    var_0 = module_0.flatten(tuple_0)
    module_1.object(*var_0)