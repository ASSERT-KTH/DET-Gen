# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import longest_common_subsequence as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    object_0 = module_0.object()
#    module_1.longest_common_subsequence(object_0, object_0)


def test_case_1():
    tuple_0 = ()
    object_0 = module_0.object()
    none_type_0 = None
    var_0 = module_1.longest_common_subsequence(none_type_0, object_0)
    assert var_0 == ""
    var_1 = module_1.longest_common_subsequence(tuple_0, object_0)
    assert var_1 == ""
    var_2 = module_1.longest_common_subsequence(object_0, var_1)
    assert var_2 == ""


#@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    var_0 = module_1.longest_common_subsequence(set_0, set_0)
    assert var_0 == ""
    var_1 = module_1.longest_common_subsequence(var_0, var_0)
    assert var_1 == ""
    bytes_0 = b"\xa9\x07\xe0\x8f"
    var_2 = module_1.longest_common_subsequence(var_0, var_1)
    assert var_2 == ""
#    module_1.longest_common_subsequence(bytes_0, bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "5?U&;3H~0T.K4X;\x0c$3"
    var_0 = module_1.longest_common_subsequence(str_0, str_0)
    assert var_0 == "5?U&;3H~0T.K4X;\x0c$3"
    var_1 = module_1.longest_common_subsequence(str_0, var_0)
    assert var_1 == "5?U&;3H~0T.K4X;\x0c$3"
    var_2 = module_1.longest_common_subsequence(var_0, var_0)
    assert var_2 == "5?U&;3H~0T.K4X;\x0c$3"
    var_3 = module_1.longest_common_subsequence(str_0, var_2)
    assert var_3 == "5?U&;3H~0T.K4X;\x0c$3"
    var_4 = module_1.longest_common_subsequence(str_0, var_2)
    assert var_4 == "5?U&;3H~0T.K4X;\x0c$3"
    none_type_0 = None
    list_0 = [none_type_0, none_type_0, none_type_0]
    var_5 = module_1.longest_common_subsequence(str_0, none_type_0)
    assert var_5 == ""
    var_6 = module_1.longest_common_subsequence(none_type_0, var_5)
    assert var_6 == ""
    str_1 = "R/\\\r0HAH"
    var_7 = module_1.longest_common_subsequence(str_1, list_0)
    assert var_7 == ""
    var_8 = module_1.longest_common_subsequence(var_6, var_2)
    assert var_8 == ""
    bool_0 = False
    set_0 = {bool_0, str_0, var_0}
    var_9 = module_1.longest_common_subsequence(none_type_0, set_0)
    assert var_9 == ""
    var_10 = module_1.longest_common_subsequence(list_0, var_0)
    assert var_10 == ""
#    module_0.object(*list_0)
