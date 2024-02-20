# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb6\xb4(\xa1\x04\xe6\xb0\x0e1}\\kG\xa0\xc1;"
    var_0 = module_0.lcs_length(bytes_0, bytes_0)
    assert var_0 == 16
    none_type_0 = None
    module_0.lcs_length(none_type_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "C9m+<CR|"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 8
    dict_0 = {}
    var_1 = module_0.lcs_length(dict_0, dict_0)
    assert var_1 == 0
    var_2 = module_0.lcs_length(dict_0, dict_0)
    assert var_2 == 0
    module_0.lcs_length(var_2, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"SM8\xea<\xa1a\xd4\xb7"
    tuple_0 = (bytes_0,)
    none_type_0 = None
    module_0.lcs_length(tuple_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    object_0 = module_1.object()
    module_0.lcs_length(none_type_0, object_0)
