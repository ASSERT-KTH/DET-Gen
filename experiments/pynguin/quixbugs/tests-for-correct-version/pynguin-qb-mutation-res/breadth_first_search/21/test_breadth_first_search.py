# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True


def test_case_1():
    int_0 = -2118
    tuple_0 = (int_0, int_0)
    node_0 = module_1.Node(successors=tuple_0, outgoing_nodes=int_0)
    var_0 = module_0.breadth_first_search(node_0, int_0)
    assert var_0 is True


def test_case_2():
    none_type_0 = None
    node_0 = module_1.Node(none_type_0)
    var_0 = module_0.breadth_first_search(node_0, none_type_0)
    assert var_0 is False