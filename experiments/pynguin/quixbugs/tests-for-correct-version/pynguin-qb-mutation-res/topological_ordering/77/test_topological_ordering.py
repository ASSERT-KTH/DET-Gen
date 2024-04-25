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
    bytes_0 = b"a\x02\xa0\x85\xcb\xae\xe1|\x15\xcb?\x8e\xfd#<\xc9#"
    module_0.topological_ordering(bytes_0)


def test_case_2():
    node_0 = module_1.Node()
    list_0 = [node_0]
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    set_0 = set()
    node_0 = module_1.Node(outgoing_nodes=set_0)
    list_0 = [node_0, node_0, set_0]
    node_1 = module_1.Node(outgoing_nodes=list_0)
    tuple_0 = (node_0, node_1)
    module_0.topological_ordering(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    node_0 = module_1.Node(successor=bool_0, incoming_nodes=bool_0)
    bool_1 = False
    dict_0 = {node_0: node_0, node_0: bool_0, node_0: bool_1, bool_0: node_0}
    module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    set_0 = set()
    node_0 = module_1.Node(outgoing_nodes=set_0)
    list_0 = [node_0, node_0, set_0]
    node_1 = module_1.Node(outgoing_nodes=list_0)
    tuple_0 = (node_1, node_1)
    module_0.topological_ordering(tuple_0)