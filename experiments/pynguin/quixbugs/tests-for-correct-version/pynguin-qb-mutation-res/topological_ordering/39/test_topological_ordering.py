# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import node as module_0
import topological_ordering as module_1


def test_case_0():
    node_0 = module_0.Node()
    set_0 = {node_0}
    var_0 = module_1.topological_ordering(set_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "e\tcZS:oECi"
    module_1.topological_ordering(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_1.topological_ordering(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -483
    node_0 = module_0.Node(incoming_nodes=int_0, outgoing_nodes=int_0)
    set_0 = {node_0}
    var_0 = module_1.topological_ordering(set_0)
    none_type_0 = None
    module_1.topological_ordering(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b""
    none_type_0 = None
    list_0 = [bytes_0]
    node_0 = module_0.Node(
        successor=bytes_0, successors=none_type_0, outgoing_nodes=list_0
    )
    set_0 = {node_0}
    module_1.topological_ordering(set_0)