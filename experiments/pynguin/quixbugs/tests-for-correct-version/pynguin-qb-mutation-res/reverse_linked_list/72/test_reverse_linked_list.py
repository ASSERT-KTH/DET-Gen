# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import reverse_linked_list as module_0
import node as module_1
import builtins as module_2


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [tuple_0]
    module_0.reverse_linked_list(list_0)


def test_case_1():
    bool_0 = False
    var_0 = module_0.reverse_linked_list(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "L1M"
    node_0 = module_1.Node(predecessors=str_0, incoming_nodes=str_0)
    var_0 = module_0.reverse_linked_list(node_0)
    assert f"{type(var_0).__module__}.{type(var_0).__qualname__}" == "node.Node"
    assert var_0.value is None
    assert var_0.successor is None
    assert var_0.successors == []
    assert var_0.predecessors == "L1M"
    assert var_0.incoming_nodes == "L1M"
    assert var_0.outgoing_nodes == []
    var_0.predecessors()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.reverse_linked_list(none_type_0)
    var_1 = module_0.reverse_linked_list(var_0)
    var_2 = module_2.object()
    node_0 = module_1.Node(successor=bool_0, outgoing_nodes=bool_0)
    module_0.reverse_linked_list(node_0)