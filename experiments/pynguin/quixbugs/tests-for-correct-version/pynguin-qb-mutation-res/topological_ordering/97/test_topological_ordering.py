# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import topological_ordering as module_0
import node as module_1


def test_case_0():
    list_0 = []
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "|zaADdap"
    module_0.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.topological_ordering(none_type_0)


def test_case_3():
    list_0 = []
    node_0 = module_1.Node(list_0)
    tuple_0 = (node_0,)
    var_0 = module_0.topological_ordering(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"ZZ.\xfcg\x7f\x97\x80\xb8\x85u\xf6\xf5\xeaq\xc4\xf7\xae\x05"
    node_0 = module_1.Node(
        bytes_0, successors=bytes_0, predecessors=bytes_0, incoming_nodes=bytes_0
    )
    list_0 = [node_0, node_0, node_0, bytes_0]
    module_0.topological_ordering(list_0)


def test_case_5():
    list_0 = []
    node_0 = module_1.Node(
        list_0, successors=list_0, predecessors=list_0, outgoing_nodes=list_0
    )
    tuple_0 = (node_0,)
    node_1 = module_1.Node(list_0, outgoing_nodes=tuple_0)
    dict_0 = {node_1: tuple_0}
    var_0 = module_0.topological_ordering(dict_0)


def test_case_6():
    list_0 = []
    node_0 = module_1.Node(list_0)
    tuple_0 = (node_0,)
    node_1 = module_1.Node(list_0, outgoing_nodes=tuple_0)
    dict_0 = {node_0: tuple_0, node_1: list_0, node_1: node_1}
    var_0 = module_0.topological_ordering(dict_0)