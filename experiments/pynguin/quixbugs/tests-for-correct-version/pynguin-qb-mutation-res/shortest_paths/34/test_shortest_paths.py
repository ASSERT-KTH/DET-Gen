# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x91\x1b"
    dict_0 = {bytes_0: bytes_0}
    module_0.shortest_paths(bytes_0, dict_0)


def test_case_1():
    bytes_0 = b""
    var_0 = module_0.shortest_paths(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.shortest_paths(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = -1633
    tuple_0 = (int_0, int_0)
    dict_0 = {tuple_0: int_0}
    var_0 = module_0.shortest_paths(tuple_0, dict_0)
    bytes_0 = b"z\xea"
    dict_1 = {
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    module_0.shortest_paths(bytes_0, dict_1)