# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0
import builtins as module_1


def test_case_0():
    str_0 = "SLA,Kca"
    var_0 = module_0.next_permutation(str_0)


def test_case_1():
    str_0 = "SLA,Kca"
    set_0 = {str_0}
    var_0 = module_0.next_permutation(set_0)
    var_1 = module_0.next_permutation(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.next_permutation(object_0)


def test_case_3():
    str_0 = "Oa9#bc!$mZzA"
    var_0 = module_0.next_permutation(str_0)