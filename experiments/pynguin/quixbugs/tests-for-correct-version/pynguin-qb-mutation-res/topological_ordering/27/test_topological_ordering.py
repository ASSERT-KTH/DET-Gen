# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    bytes_0 = b""
    var_0 = module_0.topological_ordering(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "8\x0bwSeb6JUH:B\\/7y`%:"
    module_0.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.topological_ordering(bool_0)


def test_case_3():
    node_0 = module_1.Node()
    set_0 = {node_0, node_0, node_0, node_0}
    var_0 = module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 639.1
    node_0 = module_1.Node(float_0, successors=float_0, predecessors=float_0)
    none_type_0 = None
    none_type_1 = None
    node_1 = module_1.Node(
        successor=none_type_0, successors=none_type_1, incoming_nodes=node_0
    )
    int_0 = 569
    dict_0 = {node_0: node_0, node_1: int_0}
    var_0 = module_0.topological_ordering(dict_0)
    module_0.topological_ordering(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bool_0 = False
    list_0 = [bool_0]
    dict_0 = {bool_0: bool_0, bool_0: list_0, bool_0: bool_0}
    tuple_0 = (bool_0, list_0, dict_0)
    node_0 = module_1.Node(
        tuple_0, successors=dict_0, incoming_nodes=bool_0, outgoing_nodes=dict_0
    )
    dict_1 = {node_0: bool_0}
    module_0.topological_ordering(dict_1)