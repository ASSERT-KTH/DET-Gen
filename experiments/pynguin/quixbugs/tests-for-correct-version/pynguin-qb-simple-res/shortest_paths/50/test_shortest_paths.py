# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


def test_case_0():
    bytes_0 = b""
    var_0 = module_0.shortest_paths(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"@\x9d"
    list_0 = [bytes_0]
    module_0.shortest_paths(bytes_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.shortest_paths(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xcf\xa4"
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0}
    module_0.shortest_paths(bytes_0, dict_0)


def test_case_4():
    bytes_0 = b""
    bytes_1 = b"\x00\xa4"
    var_0 = module_0.shortest_paths(bytes_1, bytes_0)
    bool_0 = False
    var_1 = module_0.shortest_paths(bool_0, var_0)