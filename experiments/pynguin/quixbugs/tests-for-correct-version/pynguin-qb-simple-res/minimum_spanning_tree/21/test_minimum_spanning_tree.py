# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    dict_0 = {}
    bool_0 = True
    dict_1 = {bool_0: bool_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    module_0.minimum_spanning_tree(dict_1)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.minimum_spanning_tree(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -3875.6
    bytes_0 = b"\xb7\x84\x99"
    tuple_0 = (float_0, bytes_0)
    dict_0 = {tuple_0: tuple_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    var_0.predecessors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = -3875.6
    tuple_0 = (float_0, float_0)
    dict_0 = {tuple_0: tuple_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    var_1 = module_0.minimum_spanning_tree(dict_0)
    var_0.predecessors()