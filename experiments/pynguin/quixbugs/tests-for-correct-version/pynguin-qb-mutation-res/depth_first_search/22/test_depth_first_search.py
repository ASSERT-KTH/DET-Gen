# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.depth_first_search(bool_0, bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    set_0 = {bool_0}
    module_0.depth_first_search(bool_0, set_0)


def test_case_2():
    node_0 = module_1.Node()
    none_type_0 = None
    var_0 = module_0.depth_first_search(node_0, none_type_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    var_0 = module_0.depth_first_search(bool_0, bool_0)
    assert var_0 is True
    node_0 = module_1.Node(successor=var_0, predecessors=var_0)
    assert node_0.successor is True
    assert node_0.predecessors is True
    var_1 = module_0.depth_first_search(node_0, var_0)
    node_1 = module_1.Node(var_0, outgoing_nodes=node_0)
    assert node_1.value is True
    var_2 = module_0.depth_first_search(bool_0, bool_0)
    assert var_2 is True
    bytes_0 = b'\xa0\xfe"hc\xfd\n\xaf\x0e\xbd\xe1&<^zH'
    complex_0 = -1984.754 - 3000.28788j
    node_2 = module_1.Node(
        successor=complex_0,
        successors=bytes_0,
        predecessors=var_0,
        incoming_nodes=var_2,
    )
    assert node_2.predecessors is True
    assert node_2.incoming_nodes is True
    module_0.depth_first_search(node_2, node_0)