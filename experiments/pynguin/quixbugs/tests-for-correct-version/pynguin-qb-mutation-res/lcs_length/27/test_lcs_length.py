# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0,)
    var_0 = module_0.lcs_length(tuple_0, tuple_0)
    assert var_0 == 1
    dict_0 = {}
    var_1 = module_0.lcs_length(dict_0, dict_0)
    assert var_1 == 0
    module_0.lcs_length(tuple_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    object_0 = module_1.object()
    dict_0 = {
        object_0: object_0,
        object_0: object_0,
        object_0: object_0,
        object_0: object_0,
    }
    module_0.lcs_length(dict_0, object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x9e=\x10\xef\xcfCb\xb7b&\xf5\xcd\xd3\xdf\xc9'\x9b\xd3?\x8e"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 20
    none_type_0 = None
    module_0.lcs_length(none_type_0, bytes_0)