# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0
import node as module_1
import builtins as module_2


def test_case_0():
    bytes_0 = b"\xda\xcf"
    dict_0 = {
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    var_0 = module_0.minimum_spanning_tree(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    node_0 = module_1.Node(bool_0, successors=bool_0, outgoing_nodes=bool_0)
    module_0.minimum_spanning_tree(node_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xda\xda"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    module_2.object(*var_0, **dict_0)