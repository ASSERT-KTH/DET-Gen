# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import longest_common_subsequence as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
#    module_0.longest_common_subsequence(bool_0, bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    var_0 = module_0.longest_common_subsequence(none_type_0, none_type_0)
    assert var_0 == ""
    bool_0 = True
#    module_0.longest_common_subsequence(bool_0, bool_0)


def test_case_2():
    str_0 = "=o~\x0cq+"
    list_0 = []
    tuple_0 = (str_0, list_0)
    var_0 = module_0.longest_common_subsequence(tuple_0, str_0)
    assert var_0 == ""


#@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1899
    dict_0 = {int_0: int_0, int_0: int_0}
    tuple_0 = (dict_0,)
#    module_0.longest_common_subsequence(tuple_0, tuple_0)
