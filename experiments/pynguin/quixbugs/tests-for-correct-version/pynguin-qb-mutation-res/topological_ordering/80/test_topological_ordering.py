# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    dict_0 = {}
    var_0 = module_0.topological_ordering(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "c&]WtOM0~..*sUvanHk"
    module_0.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.topological_ordering(bool_0)


def test_case_3():
    node_0 = module_1.Node()
    list_0 = [node_0, node_0]
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = -114
    object_0 = module_2.object()
    node_0 = module_1.Node(predecessors=int_0, incoming_nodes=object_0)
    str_0 = "h'ZX9Z%U|O\tpNM"
    set_0 = {node_0, int_0, str_0}
    module_0.topological_ordering(set_0)


def test_case_5():
    node_0 = module_1.Node()
    list_0 = [node_0, node_0]
    node_1 = module_1.Node(outgoing_nodes=list_0)
    list_1 = [node_0, node_0, node_1, node_0]
    var_0 = module_0.topological_ordering(list_1)


def test_case_6():
    node_0 = module_1.Node()
    list_0 = [node_0, node_0]
    node_1 = module_1.Node(outgoing_nodes=list_0)
    set_0 = {node_1}
    var_0 = module_0.topological_ordering(set_0)