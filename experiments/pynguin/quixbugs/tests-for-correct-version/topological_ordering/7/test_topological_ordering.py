# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    set_0 = set()
    var_0 = module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    bool_1 = True
    list_0 = [bool_0, bool_1, bool_0, bool_1]
    module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.topological_ordering(none_type_0)


def test_case_3():
    none_type_0 = None
    node_0 = module_1.Node(none_type_0, successors=none_type_0)
    set_0 = {node_0, node_0}
    var_0 = module_0.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    none_type_0 = None
    node_0 = module_1.Node(none_type_0, successors=none_type_0)
    set_0 = {node_0, node_0, none_type_0}
    module_0.topological_ordering(set_0)


def test_case_5():
    set_0 = set()
    none_type_0 = None
    set_1 = {none_type_0}
    node_0 = module_1.Node(set_0, none_type_0, incoming_nodes=set_1)
    dict_0 = {node_0: set_0, node_0: node_0}
    node_1 = module_1.Node(
        dict_0, successors=dict_0, predecessors=set_0, outgoing_nodes=dict_0
    )
    set_2 = {node_1, node_1, node_1, node_1, node_0, node_0}
    var_0 = module_0.topological_ordering(set_2)


def test_case_6():
    set_0 = set()
    node_0 = module_1.Node(set_0, set_0, incoming_nodes=set_0)
    dict_0 = {node_0: set_0, node_0: set_0}
    node_1 = module_1.Node(dict_0, successors=node_0, outgoing_nodes=dict_0)
    set_1 = {node_1, node_1}
    var_0 = module_0.topological_ordering(set_1)


def test_case_7():
    set_0 = set()
    node_0 = module_1.Node(set_0, set_0, incoming_nodes=set_0)
    dict_0 = {node_0: set_0, node_0: set_0}
    node_1 = module_1.Node(dict_0, successors=node_0, outgoing_nodes=dict_0)
    set_1 = {node_1, node_0}
    var_0 = module_0.topological_ordering(set_1)
