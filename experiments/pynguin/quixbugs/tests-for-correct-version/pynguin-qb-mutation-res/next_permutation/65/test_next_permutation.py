# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0
import builtins as module_1


def test_case_0():
    str_0 = "y)fRQy)F6C"
    var_0 = module_0.next_permutation(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    var_0 = module_0.next_permutation(tuple_0)
    var_1 = module_0.next_permutation(tuple_0)
    module_1.object(**var_0)


def test_case_2():
    str_0 = "~LDc8k<;SjN"
    var_0 = module_0.next_permutation(str_0)