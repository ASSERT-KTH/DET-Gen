# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.lcs_length(list_0, list_0)
    assert var_0 == 4
    module_0.lcs_length(list_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.lcs_length(tuple_0, tuple_0)
    assert var_0 == 0
    var_1 = module_0.lcs_length(tuple_0, tuple_0)
    assert var_1 == 0
    module_0.lcs_length(var_1, var_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.lcs_length(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "gk)BIvfU"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 8
    tuple_0 = ()
    int_0 = -3012
    var_1 = module_0.lcs_length(tuple_0, int_0)
    assert var_1 == 0
    set_0 = set()
    bool_0 = False
    bytes_0 = b"VIBE\x0c3[a\xe8\xae\x9e\x82\xae\x83\xc2\xf6"
    tuple_1 = (set_0, bool_0, bytes_0)
    var_2 = module_0.lcs_length(tuple_1, tuple_1)
    assert var_2 == 3
    object_0 = module_1.object()
    module_0.lcs_length(object_0, object_0)