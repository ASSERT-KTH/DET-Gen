# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    str_0 = ""
    var_0 = module_0.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = 'G<@]0q02)UlJhL%Y\x0c="B'
    module_0.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0)
    node_0 = module_1.Node(predecessors=tuple_0, incoming_nodes=bool_0)
    set_0 = {node_0, bool_0, node_0, tuple_0}
    module_0.topological_ordering(set_0)


def test_case_3():
    node_0 = module_1.Node()
    dict_0 = {node_0: node_0}
    var_0 = module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "5U\t 8cN[nG`Hnk%\x0br"
    str_1 = "5U\t 8cN[nG`HLk%\x0br"
    node_0 = module_1.Node(str_0, successors=str_1, outgoing_nodes=str_0)
    tuple_0 = (node_0,)
    module_0.topological_ordering(tuple_0)