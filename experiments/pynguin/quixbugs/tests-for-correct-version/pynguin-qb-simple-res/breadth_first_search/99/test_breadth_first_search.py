# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    none_type_0 = None
    var_0 = module_0.breadth_first_search(none_type_0, none_type_0)
    assert var_0 is True


def test_case_1():
    bytes_0 = b"}(\x11xE6\x88\x83\xe3\x0f\x8f\x1d\xafZ\x19\xa0/\xf7\xa9"
    node_0 = module_1.Node(incoming_nodes=bytes_0, outgoing_nodes=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert (
        node_0.incoming_nodes
        == b"}(\x11xE6\x88\x83\xe3\x0f\x8f\x1d\xafZ\x19\xa0/\xf7\xa9"
    )
    assert (
        node_0.outgoing_nodes
        == b"}(\x11xE6\x88\x83\xe3\x0f\x8f\x1d\xafZ\x19\xa0/\xf7\xa9"
    )
    var_0 = module_0.breadth_first_search(node_0, bytes_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 753.6644 + 2550.47421j
    none_type_0 = None
    module_0.breadth_first_search(complex_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"L\x02\x90?\xd8\xc7\xdf\x86{"
    node_0 = module_1.Node(successors=bytes_0, outgoing_nodes=bytes_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == b"L\x02\x90?\xd8\xc7\xdf\x86{"
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == b"L\x02\x90?\xd8\xc7\xdf\x86{"
    module_0.breadth_first_search(node_0, bytes_0)