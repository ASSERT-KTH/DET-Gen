# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import breadth_first_search as module_0
import node as module_1


def test_case_0():
    bytes_0 = b"\xb8\x12j\x85\x81\xc7\x19%\xa5d\xb6\x96"
    var_0 = module_0.breadth_first_search(bytes_0, bytes_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"[k\xa3j\x85\r\xa4n\xa7Q\xe8}]\xadsqChE"
    node_0 = module_1.Node(successors=bytes_0)
    module_0.breadth_first_search(node_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"H;\xf3\xf4\x18\x9d\xa5e}?%\xf3_\x00<Z_Q"
    node_0 = module_1.Node(outgoing_nodes=bytes_0)
    var_0 = module_0.breadth_first_search(node_0, bytes_0)
    assert var_0 is False
    var_0.successor()