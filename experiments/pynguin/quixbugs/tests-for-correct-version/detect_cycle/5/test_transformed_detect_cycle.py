# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import node as module_0
import detect_cycle as module_1


def test_case_0():
    node_0 = module_0.Node()
    node_1 = module_0.Node(successor=node_0)
    var_0 = module_1.detect_cycle(node_1)
    assert var_0 is False


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    node_0 = module_0.Node(successor=bool_0, successors=bool_0, incoming_nodes=bool_0)
#    module_1.detect_cycle(node_0)


def test_case_2():
    bool_0 = True
    node_0 = module_0.Node(successor=bool_0, successors=bool_0, incoming_nodes=bool_0)
    node_1 = module_0.Node(node_0)
    var_0 = module_1.detect_cycle(node_1)
    assert var_0 is False
