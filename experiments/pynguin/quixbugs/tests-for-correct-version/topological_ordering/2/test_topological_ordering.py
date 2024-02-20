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
    bytes_0 = b"o\x80\x8c0\xf6\x93\x83\xd4\xab"
    module_0.topological_ordering(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.topological_ordering(bool_0)


def test_case_3():
    node_0 = module_1.Node()
    list_0 = [node_0, node_0]
    var_0 = module_0.topological_ordering(list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x844+C\rA\x84\xffh\xac\xfe#n\rt\xa5!8\xdau"
    set_0 = {bytes_0, bytes_0, bytes_0}
    node_0 = module_1.Node(incoming_nodes=set_0)
    list_0 = [node_0, set_0]
    module_0.topological_ordering(list_0)


def test_case_5():
    list_0 = []
    node_0 = module_1.Node(successor=list_0, incoming_nodes=list_0)
    list_1 = [node_0]
    node_1 = module_1.Node(
        successor=list_0, successors=list_0, predecessors=node_0, outgoing_nodes=list_1
    )
    list_2 = [node_1, node_1, node_1, node_1, node_1]
    var_0 = module_0.topological_ordering(list_2)
