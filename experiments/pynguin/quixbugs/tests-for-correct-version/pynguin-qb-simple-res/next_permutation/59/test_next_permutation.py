# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    str_0 = ",8c>]gjjXKu47\x0c7"
    var_0 = module_0.next_permutation(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.next_permutation(dict_0)
    int_0 = -3084
    module_0.next_permutation(int_0)


def test_case_2():
    str_0 = ",8c>]gjjXKu47\x0c\rhr7"
    var_0 = module_0.next_permutation(str_0)