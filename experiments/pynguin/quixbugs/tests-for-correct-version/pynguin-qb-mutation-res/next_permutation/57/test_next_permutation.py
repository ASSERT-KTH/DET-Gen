# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    str_0 = "fda 4\x0bw8H],<qy1}I:"
    var_0 = module_0.next_permutation(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1149
    dict_0 = {int_0: int_0, int_0: int_0}
    var_0 = module_0.next_permutation(dict_0)
    int_1 = -2841
    module_0.next_permutation(int_1)


def test_case_2():
    str_0 = "fda 4\x0bw8H],<qy1}I/"
    var_0 = module_0.next_permutation(str_0)