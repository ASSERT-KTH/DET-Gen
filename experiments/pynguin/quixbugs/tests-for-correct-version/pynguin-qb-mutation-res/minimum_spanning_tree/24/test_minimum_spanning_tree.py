# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0
import node as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    tuple_0 = ()
    var_0 = module_0.minimum_spanning_tree(tuple_0)
    dict_0 = {tuple_0: tuple_0, tuple_0: tuple_0, tuple_0: tuple_0}
    module_0.minimum_spanning_tree(dict_0)


def test_case_1():
    bytes_0 = b""
    var_0 = module_0.minimum_spanning_tree(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.minimum_spanning_tree(none_type_0)


def test_case_3():
    int_0 = -718
    tuple_0 = (int_0, int_0)
    dict_0 = {
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
        tuple_0: tuple_0,
    }
    var_0 = module_0.minimum_spanning_tree(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    tuple_0 = ()
    var_0 = module_1.Node(tuple_0, tuple_0, incoming_nodes=tuple_0)
    var_1 = module_0.minimum_spanning_tree(tuple_0)
    int_0 = -702
    tuple_1 = (var_0, int_0)
    dict_0 = {tuple_1: int_0, tuple_0: int_0}
    module_0.minimum_spanning_tree(dict_0)