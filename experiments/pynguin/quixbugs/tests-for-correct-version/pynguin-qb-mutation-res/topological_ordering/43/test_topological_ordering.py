# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    dict_0 = {}
    var_0 = module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ")8^Jy:$Eas"
    bool_0 = False
    tuple_0 = (str_0, bool_0)
    module_0.topological_ordering(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = -1429.37 - 1545.95721j
    module_0.topological_ordering(complex_0)


def test_case_3():
    dict_0 = {}
    node_0 = module_1.Node(successor=dict_0, outgoing_nodes=dict_0)
    tuple_0 = (node_0, node_0, node_0, node_0)
    node_1 = module_1.Node(node_0, outgoing_nodes=tuple_0)
    list_0 = [node_1]
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "S"
    dict_0 = {str_0: str_0}
    node_0 = module_1.Node(dict_0, predecessors=dict_0)
    dict_1 = {node_0: node_0, str_0: node_0, node_0: dict_0}
    module_0.topological_ordering(dict_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = True
    node_0 = module_1.Node(incoming_nodes=bool_0)
    list_0 = [bool_0]
    dict_0 = {node_0: node_0, bool_0: list_0, node_0: node_0, node_0: list_0}
    module_0.topological_ordering(dict_0)