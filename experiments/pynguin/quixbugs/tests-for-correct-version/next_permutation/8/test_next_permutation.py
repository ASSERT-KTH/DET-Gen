# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    str_0 = "FOy^@r\\1N+"
    var_0 = module_0.next_permutation(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    set_0 = set()
    var_0 = module_0.next_permutation(set_0)
    var_1 = module_0.next_permutation(set_0)
    none_type_0 = None
    module_0.next_permutation(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.next_permutation(none_type_0)
