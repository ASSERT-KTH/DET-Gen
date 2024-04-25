# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    bool_0 = True
    var_0 = module_0.breadth_first_search(bool_0, bool_0)
    assert var_0 is True


def test_case_1():
    node_0 = module_1.Node()
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    str_0 = "^C&8Y=ul~H0&$-]"
    var_0 = module_0.breadth_first_search(node_0, str_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '2K(ry`@"84.@&w^PM!'
    node_0 = module_1.Node(successors=str_0, predecessors=str_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == '2K(ry`@"84.@&w^PM!'
    assert node_0.predecessors == '2K(ry`@"84.@&w^PM!'
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.breadth_first_search(node_0, str_0)