# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import longest_common_subsequence as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
    module_1.longest_common_subsequence(object_0, object_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_1.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""
    var_1 = module_1.longest_common_subsequence(none_type_0, var_0)
    assert var_1 == ""
    var_2 = module_1.longest_common_subsequence(var_1, var_1)
    assert var_2 == ""


def test_case_2():
    object_0 = module_0.object()
    dict_0 = {
        object_0: object_0,
        object_0: object_0,
        object_0: object_0,
        object_0: object_0,
    }
    tuple_0 = (object_0, dict_0, object_0)
    none_type_0 = None
    var_0 = module_1.longest_common_subsequence(tuple_0, none_type_0)
    assert var_0 == ""


@pytest.mark.xfail(strict=True)
def test_case_3():
    none_type_0 = None
    var_0 = module_1.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""
    var_1 = module_1.longest_common_subsequence(none_type_0, var_0)
    assert var_1 == ""
    var_2 = module_1.longest_common_subsequence(none_type_0, none_type_0)
    assert var_2 == ""
    list_0 = [none_type_0]
    module_1.longest_common_subsequence(list_0, list_0)


def test_case_4():
    bool_0 = False
    bytes_0 = b""
    str_0 = "27a. M}>sl\x0cXat<"
    tuple_0 = (bytes_0, bool_0, bytes_0, str_0)
    tuple_1 = (bool_0, tuple_0)
    tuple_2 = (tuple_1,)
    var_0 = module_1.longest_common_subsequence(tuple_2, tuple_1)
    assert var_0 == ""
    bool_1 = False
    var_1 = module_1.longest_common_subsequence(bool_1, bool_1)
    assert var_1 == ""
    var_2 = module_1.longest_common_subsequence(var_1, var_1)
    assert var_2 == ""
    var_3 = module_1.longest_common_subsequence(var_1, var_1)
    assert var_3 == ""
    var_4 = module_1.longest_common_subsequence(var_3, var_1)
    assert var_4 == ""