# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import depth_first_search as module_0
import node as module_1


def test_case_0():
    str_0 = '(I@e3yrm"\r5>T|O\x0bu'
    var_0 = module_0.depth_first_search(str_0, str_0)
    assert var_0 is True


def test_case_1():
    none_type_0 = None
    node_0 = module_1.Node(outgoing_nodes=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is None
    var_0 = module_0.depth_first_search(node_0, none_type_0)
    assert var_0 is False


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -1900.434211
    bool_0 = True
    dict_0 = {float_0: bool_0, float_0: float_0, float_0: bool_0}
    none_type_0 = None
    node_0 = module_1.Node(successors=dict_0, predecessors=none_type_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert (
        f"{type(node_0.successors).__module__}.{type(node_0.successors).__qualname__}"
        == "builtins.dict"
    )
    assert len(node_0.successors) == 1
    assert node_0.predecessors is None
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes == []
    module_0.depth_first_search(node_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    node_0 = module_1.Node(outgoing_nodes=bool_0)
    assert f"{type(node_0).__module__}.{type(node_0).__qualname__}" == "node.Node"
    assert node_0.value is None
    assert node_0.successor is None
    assert node_0.successors == []
    assert node_0.predecessors == []
    assert node_0.incoming_nodes == []
    assert node_0.outgoing_nodes is False
    list_0 = [node_0, node_0]
    dict_0 = {node_0: bool_0}
    bytes_0 = b"{\xacd\x98\x98\xc4\xbf/\xe3\x14b"
    tuple_0 = (list_0, dict_0, bytes_0, node_0)
    node_1 = module_1.Node(tuple_0, successors=list_0)
    assert f"{type(node_1).__module__}.{type(node_1).__qualname__}" == "node.Node"
    assert (
        f"{type(node_1.value).__module__}.{type(node_1.value).__qualname__}"
        == "builtins.tuple"
    )
    assert len(node_1.value) == 4
    assert node_1.successor is None
    assert (
        f"{type(node_1.successors).__module__}.{type(node_1.successors).__qualname__}"
        == "builtins.list"
    )
    assert len(node_1.successors) == 2
    assert node_1.predecessors == []
    assert node_1.incoming_nodes == []
    assert node_1.outgoing_nodes == []
    var_0 = module_0.depth_first_search(node_1, bytes_0)
    assert var_0 is False
    str_0 = "]c"
    float_0 = 432.134
    module_0.depth_first_search(str_0, float_0)