# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"B\xfa"
    list_0 = []
    var_0 = module_0.shortest_paths(bytes_0, list_0)
    module_0.shortest_paths(bytes_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -3420
    module_0.shortest_paths(int_0, int_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x0b\x0b"
    list_0 = []
    var_0 = module_0.shortest_paths(bytes_0, list_0)
    var_1 = module_0.shortest_paths(bytes_0, var_0)
    module_0.shortest_paths(list_0, var_1)