# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import node as module_0
import detect_cycle as module_1


def test_case_0():
    bool_0 = False
    var_0 = module_0.Node(
        successors=bool_0, incoming_nodes=bool_0, outgoing_nodes=bool_0
    )
    node_0 = module_0.Node(successor=var_0, predecessors=var_0)
    var_1 = module_1.detect_cycle(node_0)
    assert var_1 is False


def test_case_1():
    bool_0 = False
    node_0 = module_0.Node(predecessors=bool_0)
    var_0 = module_1.detect_cycle(node_0)
    assert var_0 is False
    node_1 = module_0.Node(successor=node_0, predecessors=node_0)
    var_1 = module_1.detect_cycle(node_1)
    assert var_1 is False