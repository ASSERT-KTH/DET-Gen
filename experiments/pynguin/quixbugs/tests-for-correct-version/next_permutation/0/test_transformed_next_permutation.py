# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    str_0 = "lXW1B\tx"
    var_0 = module_0.next_permutation(str_0)


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    bool_0 = True
    bool_1 = False
    var_0 = module_0.next_permutation(list_0)
    dict_0 = {bool_0: list_0}
    var_1 = module_0.next_permutation(dict_0)
#    module_0.next_permutation(bool_1)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
#    module_0.next_permutation(none_type_0)


def test_case_3():
    str_0 = "n$ix#"
    var_0 = module_0.next_permutation(str_0)
